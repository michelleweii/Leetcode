class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # tmp=""
        max_length=0
        max_string=""
        for i in range(len(s)):
            # print(s[i:len(s)])
            tmp = ""
            for letter in s[i:len(s)]:
                tmp+=letter
                # print(tmp)
                if tmp==tmp[::-1]:
                    if len(tmp)>max_length:
                        max_length=len(tmp)
                        max_string=tmp
        # print(max_string)
        return max_string





if __name__ == '__main__':
    s = "babad"
    myResult = Solution()
    print(myResult.longestPalindrome(s))