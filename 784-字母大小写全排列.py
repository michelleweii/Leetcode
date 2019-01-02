class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

    def letterCasePermutation1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for s in S:
            if not s.isalpha():
                for i in range(len(res)):
                    res[i] += s
            else:
                for i in range(len(res)):
                    tmp = res[i]
                    res[i] += s.lower()
                    res.append(tmp + s.upper())
        return res


def main():
    S = "a1b2"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.letterCasePermutation(S))

if __name__ == '__main__':
    main()