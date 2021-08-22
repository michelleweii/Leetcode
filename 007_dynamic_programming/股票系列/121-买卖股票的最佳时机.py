class Solution(object):
    def maxProfit(self, prices):
        # 在价格最低的时候买入，差价最大的时候卖出
        if len(prices) < 2: return 0
        cost = prices[0]
        profit = 0
        for price in prices:
            cost = min(cost, price) # 找到最低那天的价格
            profit = max(profit, price-cost)
        return profit

    # dp
    # 只要考虑当天买和之前买哪个收益更高，当天卖和之前卖哪个收益更高
    #     dp = [[0, 0] for i in range(len(prices))]
    #     if not prices:return 0
    #     dp[-1][1] = -float("inf")
    #     for i in range(len(prices)):
    #         dp[i][1] = max(dp[i - 1][1], -prices[i])
    #         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    #     return dp[-1][0]


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))