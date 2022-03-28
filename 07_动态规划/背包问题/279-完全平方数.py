"""
middle 2022-03-17 不带顺序的完全背包
# dp[i]：表示完全平方数和为i的 最小个数
# 初始状态dp[i]均取最大值i，即 1+1+...+1，i个1; dp[0] = 0
# dp[i] = min(dp[i], dp[i-j*j]+1)，其中, j是平方数, j=1~k,其中k*k要保证 <= i
# 意思就是：完全平方数和为i的 最小个数 等于 当前完全平方数和为i的 最大个数
#   与 （完全平方数和为 i - j * j 的 最小个数 + 完全平方数和为 j * j的 最小个数）
#   可以看到 dp[j*j] 是等于1的
"""
class Solution:
    def numSquares(self, n: int) -> int:
        # 不要求顺序的完全背包13=4+9，13=9+4
        # 初始化一个大值（不能达到的）
        dp = [0] + [n] * n # [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
        rg = int(n**0.5) # 开根
        # 遍历arrs
        for i in range(1, rg + 1): # 1.2.3
            curr = i * i # 1.4.9
            # 遍历target
            for j in range(curr,n+1):
                dp[j] = min(dp[j],dp[j-curr]+1)
        return dp[n]

if __name__ == '__main__':
    n = 12
    print(Solution().numSquares(n)) # 4+4+4 3个