# list的每个位置都保留到目前位置，list的最大的和。
class Solution(object):
    def maxSubArray(self, nums):
        # length = len(nums)
        # for i in range(1,length):
        #     num = max(nums[i]+nums[i-1],nums[i])
        #     nums[i] = num
        #     # print(num)
        # # print(nums)     # [-2, 1, -2, 4, 3, 5, 6, 1, 5]
        # return max(nums)
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    myResult = Solution()
    print(myResult.maxSubArray(nums))


if __name__ == '__main__':
    main()
