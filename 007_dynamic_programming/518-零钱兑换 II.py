"""
middle
动态规划
是否可以用 coins 中的数组合和成 amount，完全背包问题，并且为“不考虑排列顺序的完全背包问题”，外层循环为选择池 coins，内层循环为 amount。
dp[i] 表示和为 i 的 coin 组合有 dp[i] 种。
"""
# link:https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
class Solution:
    def change(self, amount, coins):
        # dp[i]是构成金额i的硬币数目
        dp = [0 for _ in range(amount)]
        for i in range(amount):
            for j in range(len(coins)):
                dp[i] = dp[i - coins[j]] + 1

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount,coins))