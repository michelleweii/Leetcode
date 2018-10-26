# ac
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        # print(s)
        news = ""
        # s[1].is
        for i in range(len(s)):
            if s[i].isalnum(): # 题目要求：只考虑字母和数字字符
                news+=s[i]
        # print(news)
        # news = 'aba'
        length = len(news)
        for i in range(length//2):
            if news[i] != news[length-i-1]:
                return False
        return True

def main():
    s = "A man, a plan, a canal: Panama"
    myResult = Solution()
    print(myResult.isPalindrome(s))

if __name__ == '__main__':
    main()