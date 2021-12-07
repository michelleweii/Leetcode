"""
middle 2021-12-08 超级常考
!!!要求连续
"""
# 给定一个整数数组nums，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
class Solution:
    def maxProduct(self, nums):
        # dp[i], 以i结尾的数组，乘积最大
        dp = [0]*(len(nums)+1)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],nums[i]*dp[i-1])
            # print(dp[i])
        return max(dp)

if __name__ == '__main__':
    nums = [2,3,-2,4]
    print(Solution().maxProduct(nums))