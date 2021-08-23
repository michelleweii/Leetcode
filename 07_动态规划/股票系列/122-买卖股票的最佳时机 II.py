"""
    # 0 持有现金
    # 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
"""
class Solution:
    def maxProfit(self, prices):
        if not prices:return 0
        if len(prices)==1:return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[-1][1] = -float("inf")
        for i in range(n):
            # [0]现金状态，从持有股票的状态转来，再加上卖出股票的利润
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # [1]持股状态，从现金状态转来，再减去买入股票的价格
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]

    # 贪心做法，每天都可以买卖
    #     sum_num = 0
    #     for i in range(n - 1):
    #         if prices[i] < prices[i + 1]:
    #             sum_num += prices[i + 1] - prices[i]
    #     return sum_num


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))