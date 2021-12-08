"""
middle 2021-12-08
一维dp, # dp[i]是以第i个元素结尾的最长上升子序列
- 数组：要求连续i-1,i,i+1
- 子序列：不要求连续i-3,i,i+5
"""
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums)==0:return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                # 当前元素要比之前的元素大，才可以跟在后面，构成上升
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1) # dp[j] 是之前元素的最大值
        return max(dp)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))