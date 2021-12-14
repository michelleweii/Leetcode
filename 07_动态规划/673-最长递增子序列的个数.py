"""
middle 2019-03-14 dp
https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-dp673-9txt/
# lc300是求最长上升子序列的长度是是多少，是求len
# 这道题是求最长上升子序列那个最长的那个一共有多少个，多少组，有多少个可能性构成

"""
class Solution:
    def findNumberOfLIS(self, nums):
        res = 0
        max_len = 1
        # dp[i]是以第i个元素结尾的最长递增子序列的长度
        dp = [1 for _ in range(len(nums))]
        # 每个递增序列对应的子序列的个数
        cnt = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j]
                elif nums[i]>nums[j] and dp[i] == dp[j]+1:
                    cnt[i] += cnt[j]
            max_len = max(max_len,dp[i])
        print(dp)
        print(cnt)
        for k in range(len(nums)):
            if dp[k] == max_len:
                res += cnt[k]
        return res

if __name__ == '__main__':
    nums = [2,2,2,2,2]
    # nums = [1,3,5,4,7]
    print(Solution().findNumberOfLIS(nums))
    # print(Solution().fn(nums))
