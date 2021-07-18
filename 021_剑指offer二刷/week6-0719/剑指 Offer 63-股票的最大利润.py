"""
middle 一维dp
"""
# dp[i] 为 第i天卖出的最大利润
# 扩展可以交易两次（买卖算一次交易）求最大值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            for j in range(0,i):
            dp[i] = dp[i]-min()

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))