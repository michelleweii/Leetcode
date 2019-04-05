# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

#  * 动态规划：dp[i]表示在第i天(0~i)所能获得的最大利润，第i天的状态由前一天是买入还是卖出还是冷冻决定
#
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        buy,sell,cooldown = [0 for _ in range(n)],[0 for _ in range(n)],[0 for _ in range(n)]
        # 第一天不能卖，冷冻，但是可以买入
        buy[0] = -prices[0]

        for i in range(1,n):
            # 第i天是卖出，说明i-1也是可以卖出 or i-1是刚买入
            sell[i] = max(buy[i-1]+prices[i],sell[i-1])

            # 第i天是冷冻期，说明刚卖完
            cooldown[i] = sell[i-1]

            # 第i天是买入，说明i-1是冷冻期 or i-1天也可以买入
            buy[i] = max(buy[i-1],cooldown[i-1]-prices[i])

        # 一定是最后一天卖出或者最后一天冻结(刚卖完)利润最大
        return max(sell[-1],cooldown[-1])



# https://blog.csdn.net/qq_17550379/article/details/82856452
if __name__ == '__main__':
    prices = [1,2,3,0,2]
    # 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
    print(Solution().maxProfit(prices))