class Solution(object):
    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 设dp[i]为构成金额i的最优解,即凑成总金额所需的最少的硬币个数
        # 那么dp[1]=1,dp[2]=1,dp[5]=1,因为coins中有此金额，直接拿来用即可
        # dp[i]=min(dp[i-1],dp[i-2],dp[i-5])+1

        if amount<=0: return 0
        # 初始化（这种方式初始化就不会dp越界）
        max_int = 2<<31
        dp = []
        for i in range(amount+1):
            if i not in coins:
                dp.append(max_int)
            else:
                dp.append(1)

        # 求最少硬币个数
        for i in range(amount+1):
            if i not in coins:
                for j in range(len(coins)):
                    if i-coins[j]>0:
                        dp[i] = min(dp[i-coins[j]]+1,dp[i])

        return dp[amount] if dp[amount]!=max_int else -1

    def coinChange(self, coins, amount):
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if i >= coins[j] and dp[i - coins[j]] != -1:
                    if dp[i] == -1 or dp[i] > dp[i - coins[j]] + 1:
                        dp[i] = dp[i - coins[j]] + 1
        return dp[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins,amount))



