class Solution:
    def maxProfit(self, prices):
        # 贪心算法，今天比明天赚就买入
        profit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit += prices[i+1]-prices[i]
        print(profit)




if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))