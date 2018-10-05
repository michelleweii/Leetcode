# 用dict
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 字典:
        if len(s)==1:
            return False
        dict = {}
        for i in s:
            if i not in dict.keys():
                dict[i] = 1
            else:
                count = dict[i]
                count += 1
                dict[i] = count
        print(dict) # {'a': 3, 'b': 3}
        print(dict.keys()) # dict_keys(['a', 'b'])
        print(dict.items()) # dict_items([('a', 3), ('b', 3)])
        print(dict.values()) # dict_values([3, 3])
        tmp = list(dict.values())
        print(tmp) # [3, 3]
        j = 1
        for j in range(len(tmp)):
            if tmp[j]!=tmp[j-1]:
                return False
            return True


def main():
    s = "ababba"
    myResult = Solution()
    print(myResult.repeatedSubstringPattern(s))

if __name__ == '__main__':
    main()