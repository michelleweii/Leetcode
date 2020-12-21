# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
# 假设每一种面额的硬币有无限个。
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