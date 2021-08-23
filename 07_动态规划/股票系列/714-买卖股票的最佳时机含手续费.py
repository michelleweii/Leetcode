"""
    # 0 持有现金
    # 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
"""
class Solution:
    def maxProfit(self, prices, fee):
        if not prices: return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        # print(dp)
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]-fee
        dp[-1][1] = -float("inf") # 还没有开始交易，不可能持有股票
        # dp[0][1] = -float("inf")
        for i in range(n):
            # 从持有现金的状态，转为持有股票的状态
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]-fee)
            # 从持有股票的状态，转为持有现金的状态
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        return dp[-1][0]

if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices,fee))