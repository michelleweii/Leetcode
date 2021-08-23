"""
    # 0 持有现金
    # 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
"""
class Solution:
    def maxProfit(self, k, prices):
        if not prices:return 0
        if len(prices)==1:return 0
        n = len(prices)

        # 说明我可以一天买，一天卖，退化成122的贪心做法，可以交易无限次
        if k >= (n // 2):
            sum_num = 0
            for i in range(n - 1):
                if prices[i] < prices[i + 1]:
                    sum_num += prices[i + 1] - prices[i]
            return sum_num

        dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]
        # print(dp)
        # -1天，没有开始交易，所以持股也是不存在的状态
        for j in range(k+1):
            dp[-1][j][1] = -float("inf")
        # 一次都不交易，持有股票也是不存在的状态
        for i in range(n):
            dp[i][0][1] = -float("inf")
        for i in range(n):
            for j in range(1, k+1):# 最多只能买卖k次
                #
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                # [1]，从现金状态买入股票，转为持有股票状态
                # 买入一次，减去一次交易机会
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        return dp[-1][k][0]

if __name__ == '__main__':
    # k = 2
    # prices = [3, 2, 6, 5, 0, 3]
    k = 1
    prices = [6,1,6,4,3,0,2] #5
    print(Solution().maxProfit(k, prices))