"""
middle 2021-11-08
二维动态规划
https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/
dp[i][j]表示 s1 的前i个(s[i-1])个字符和 s2 的前j个字符是否能构成 s3 的前i+j个字符。
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1,len2,len3 = len(s1),len(s2),len(s3)
        if len1+len2 != len3:return False
        # dp[i][j]表示 s1 的前i个(s[i-1])个字符和 s2 的前j个字符是否能构成 s3 的前i+j个字符。
        # dp=[[False]*(len2+1) for i in range(len1+1)]
        dp = [[False for i in range(len2+1)] for j in range(len1+1)]
        # 定义出口
        dp[0][0] = True
        # 定义边界
        # s1的前i位是否能构成s3的前i位
        for i in range(1, len1+1):
            # 前i-1位可以构成s3的前i-1位，且s1的第i位（s1[i-1]）等于s3的第i位（s3[i-1]）
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]

        # s2的前i位是否能构成s3的前i位
        for i in range(1, len2+1):
            # 前i-1位可以构成s3的前i-1位，且s2的第i位（s2[i-1]）等于s3的第i位（s3[i-1]）
            dp[0][i] = dp[0][i-1] and s2[i-1]==s3[i-1]

        # 状态转移方程
        # s1的前i位和s2的前j位能否构成s3的前i+j(i+j-1)位，取决于2种情况
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # s1 的前 i 个字符和 s2 的前 j−1 个字符能否构成 s3 的前 i+j−1 位，
                # 且 s2 的第 j 位（s2[j−1]）是否等于 s3 的第 i+j 位（s3[i+j−1]）。
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) \
                           or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[-1][-1]   # return dp[len1][len2]

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1, s2, s3))