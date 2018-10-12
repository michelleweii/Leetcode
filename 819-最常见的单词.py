# Python中字符串自带的split方法一次只能使用一个字符对字符串进行分割，但是python的正则模块则可以实现多个字符分割
# 我的思路：
# 通过split将每个单词划分开，在用字典遍历存储每一个单词，如果单词是ban的话，就不进入字典。
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # a = 'one1two2three3four4five5'
        # print(re.split('\d+', a))

        # para = paragraph.split(",")
        # print(para)
        para = re.split(" |,|\.|\s+''",paragraph)
        print(para)
        dict = {}
        # print(ban)
        for i in para:
            print(i)
            if i not in dict.keys() and i!=banned:
                dict[i] = 1
            if i!=banned:
                count = dict[i]
                count+=1
                dict[i]=count
        print(dict.get())

def main():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    myResult = Solution()
    print(myResult.mostCommonWord(paragraph, banned))

if __name__ == '__main__':
    main()



