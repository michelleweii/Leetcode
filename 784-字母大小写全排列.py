class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """





def main():
    S = "a1b2"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.letterCasePermutation(S))

if __name__ == '__main__':
    main()