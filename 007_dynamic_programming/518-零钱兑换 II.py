"""
middle 2021-08-18
动态规划
是否可以用 coins 中的数组合和成 amount，完全背包问题，并且为“不考虑排列顺序的完全背包问题”，外层循环为选择池 coins，内层循环为 amount。
dp[i] 表示和为 i 的 coin 组合有 dp[i] 种。
"""
# link:https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
class Solution:
    def change(self, amount, coins):
        # dp[i]是构成金额i的硬币数目
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1 # 只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案
        for coin in coins:
            for i in range(amount+1):
                if i>=coin:
                    dp[i] += dp[i - coin]
        return dp[amount]

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount,coins))