class Solution:
    def maxProfit(self,prices,fee):
        n = len(prices)
        buy = [0 for _ in range(n)] # 买入
        sell = [0 for _ in range(n)] # 卖出
        buy[0] = -prices[0]
        for i in range(1,n):
            # 如果不卖的话，此时还和i-1时一样；
            # 如果卖出的话，此时的最大利润是买入时的最大利润+当前的价格-手续费
            sell[i] = max(sell[i-1],buy[i-1]+prices[i]-fee)
            # 如果不买的话，此时还和i-1时一样；
            # 如果买的话，此时的最大利润是卖出时的最大利润-当前（买入时）的价格，手续费付一次
            buy[i] = max(buy[i-1],sell[i-1]-prices[i])
        return sell[-1]


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices,fee))