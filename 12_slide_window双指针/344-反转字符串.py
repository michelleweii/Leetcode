"""
easy
双指针
"""
class Solution:
    def reverseString(self, s):
        i = 0
        j = len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        return s


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    myResult = Solution()
    print(myResult.reverseString(s))