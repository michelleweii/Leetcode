class Solution(object):
    def maxProfit(self, prices):

        # 在价格最低的时候买入，差价最大的时候卖出
        if len(prices) < 2:
            return 0
        minval = prices[0]
        profit = 0
        for val in prices:
            minval = min(minval,val)
            # print(minval)
            profit = max(profit,val-minval)
            # print(profit)
        return profit


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))