
"""
    # 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
    # 0 持有现金
    # 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
"""
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        if len(prices) == 1: return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[-1][1] = -float('inf')
        dp[-2][1] = -float('inf')
        for i in range(n):
            # 买股票，可以什么都不做，可以从持有现金状态减去附加条件，转为持有股票状态
            # i-2, 因为有一天冷冻期，需要从i-2日的现金状态转移
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        return dp[-1][0]


if __name__ == '__main__':
    prices = [1,2,3,0,2]
    print(Solution().maxProfit(prices))