"""
middle 2021-07-12 二维dp
https://leetcode-cn.com/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/
"""
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if not text1 or not text2:return 0
        n, m = len(text1), len(text2)
        # n,m
        # dp[i][j], 所有text1[0-(i-1)], text2[0-(j-1)]的公共子序列集合，max。
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                # 举个例子，比如对于 ace 和 bc 而言，
                # 他们的最长公共子序列的长度等于 ① ace 和 b 的最长公共子序列长度0;
                # ② ac 和 bc 的最长公共子序列长度1 的最大值，即 1。
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        return dp[n][m]

if __name__ == '__main__':
    text1 = "abc"
    text2 = "ab"
    print(Solution().longestCommonSubsequence(text1, text2))