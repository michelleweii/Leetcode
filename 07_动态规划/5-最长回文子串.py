"""
middle 2021-12-06 动态规划
相关题目647、132
# dp[i][j] 表示 s[i, j] 是否是回文串
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        begin, max_len = 0, 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    # 记录回文串的起始位置
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        begin = i

        return s[begin:begin+max_len]

if __name__ == '__main__':
    s = "cbbd"
    print(Solution().longestPalindrome(s))