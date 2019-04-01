class Solution:
    def maxProfit(self, prices):
        # dp[i]表示以第i天为止，所获得的最大收益
        if len(prices)<2:
            return 0
        dp = [0 for _ in range(len(prices))]
        dp[0] = 0
        profit = 0
        minval = prices[0]
        for idx,val in enumerate(prices):
            minval = min(minval,val)
            profit = max(profit,val-minval)
            if profit>dp[idx]:
                dp[idx]=profit

        print(dp)



if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))