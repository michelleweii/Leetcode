# 排序列表，从后往前遍历排序的列表，再遍历单词的子序列在不在列表中，若全在则把该单词加进结果列表中。
# 最后找出结果列表中最长的单词，若多个单词长度一样，则选择字典序最前的。

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """




def main():
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    myresult = Solution()
    print(myresult.longestWord(words))

if __name__ == "__main__":
    main()
