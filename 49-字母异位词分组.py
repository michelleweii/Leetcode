import collections
class Solution(object):
    def groupAnagramsmine(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rs = []
        di = dict()
        index = 0
        for str in strs:
            tmp = []
            for char in str:
                tmp.append(char)
            ans = "".join(sorted(tmp))
            # print(ans)
            if ans in di:
                # di[ans] += 1
                # 这里rs的下标怎么弄? 字典的value是返回list的index.
                # rs[0].append(str) [['eat', 'tea', 'ate', 'nat'], ['tan'], ['bat']]
                rs[di[ans]].append(str)
            else:
                di[ans] = index
                rs.append([str])
                index += 1
            # print(di)
            # print(rs)
        return rs

    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        print(list(groups))
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(map(sorted, groups.values()))

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.groupAnagrams(strs))
    # print('----------------------------')
    # import itertools
    # # from itertools import permutations
    # print(list(itertools.permutations([1, 2, 3], 3)))

if __name__ == '__main__':
    main()