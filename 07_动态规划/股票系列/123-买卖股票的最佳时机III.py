"""
    # 0 持有现金
    # 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
"""
class Solution:
    def maxProfit(self, prices):
        if not prices:return 0
        if len(prices)==1:return 0
        n = len(prices)
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        # print(dp)
        for j in range(3): # 存在0\1\2笔交易数状态
            dp[-1][j][1] = -float("inf")
        # 一次都不交易，持有股票也是不存在的状态
        for i in range(n):
            dp[i][0][1] = -float("inf")
        for i in range(n):
            for j in range(1,3):# 最多只能买卖2次
                #
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                # [1]，从现金状态买入股票，转为持有股票状态
                # 买入一次，减去一次交易机会
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        return dp[-1][2][0]

if __name__ == '__main__':
    # prices = [3,3,5,0,0,3,1,4]
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))