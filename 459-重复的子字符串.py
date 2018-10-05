# 用dict
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        coms = list(set(s))
        len_coms = len(coms)
        for i in range(len(s)):
            if s[i:i+len_coms] != coms:
                return False
            i = i+coms


def main():
    s = "ababba"
    myResult = Solution()
    print(myResult.repeatedSubstringPattern(s))

if __name__ == '__main__':
    main()

    # # 字典:
    # # s = "ababba"
    # if len(s)==1:
    #     return False
    # dict = {}
    # for i in s:
    #     if i not in dict.keys():
    #         dict[i] = 1
    #     else:
    #         count = dict[i]
    #         count += 1
    #         dict[i] = count
    # print(dict) # {'a': 3, 'b': 3}
    # print(dict.keys()) # dict_keys(['a', 'b'])
    # print(dict.items()) # dict_items([('a', 3), ('b', 3)])
    # print(dict.values()) # dict_values([3, 3])
    # tmp = list(dict.values())
    # print(tmp) # [3, 3]