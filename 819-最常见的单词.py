# Python中字符串自带的split方法一次只能使用一个字符对字符串进行分割，但是python的正则模块则可以实现多个字符分割
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        a = "Hello world!How are you?My friend.Tom"

        # a = 'one1two2three3four4five5'
        # print(re.split('\d+', a))
        # para = paragraph.split(",")
        # print(para)
        print(re.split("_#",paragraph))
        # print(paragraph)

def main():
    paragraph = "Bob hit_ a ball, the hit #BALL flew far after it was hit."
    banned = ["hit"]
    myResult = Solution()
    print(myResult.mostCommonWord(paragraph, banned))

if __name__ == '__main__':
    main()



