class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 设dp[i]为构成金额i的最优解,即凑成总金额所需的最少的硬币个数
        # 那么dp[1]=1,dp[2]=1,dp[5]=1,因为coins中有此金额，直接拿来用即可
        # dp[i]=min(dp[i-1],dp[i-2],dp[i-5])+1

        if amount<=0:return -1

        # 初始化
        dp = [-1 for _ in range(amount+1)]


        # 求最少硬币个数
        for i in range(amount+1):
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[coins[j]]=1
                else:
                    break
                if i-coins[j]>= 0 and dp[i-coins[j]]!=-1:
                    if j==0:
                        dp[i] = dp[i - coins[j]] + 1
                    if dp[i-coins[j]]<dp[i]:
                        dp[i]=dp[i-coins[j]]+1

            # print(dp[i])
        return dp[-1]




if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins,amount))