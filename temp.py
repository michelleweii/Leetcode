# -*- coding:utf-8 -*-
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(needle==""):
            return 0
        if needle not in haystack:
            return -1
        flag = []
        for i,vaL_i in enumerate(haystack):
            if(vaL_i == needle[0]):
                flag.append(i)
        for j in flag:
            for k in range(len(needle)):
                if(haystack[j+k] != needle[k]):
                    break
                if((k+1)==len(needle)):
                    return j
            rs = j
        return rs

def main():
    haystack = "aaa"
    needle = "aa"
    rs = Solution()
    print(rs.strStr(haystack,needle))

if __name__ == '__main__':
    main()
