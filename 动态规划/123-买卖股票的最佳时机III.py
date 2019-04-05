# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        sell1,sell2 = 0,0
        # 一开始不能卖，但是可以买
        buy1,buy2 = -prices[0],-prices[0]

        # 只要考虑当天买和之前买哪个收益更高，当天卖和之前卖哪个收益更高
        for i in range(1,n):
            # i时刻的最大利润
            buy1 = max(buy1,-prices[i])
            # 当天卖出总的收益就是buy+prices[i]
            sell1 = max(sell1,buy1+prices[i])

            buy2 = max(buy2, sell1-prices[i])
            sell2 = max(sell2, buy2+prices[i])

        # 卖一次的收益大，还是卖两次的收益大
        print(sell1)
        print(sell2)
        return max(sell1,sell2)

# https://blog.csdn.net/qq_17550379/article/details/83620892
if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))