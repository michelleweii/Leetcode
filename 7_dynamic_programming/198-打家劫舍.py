class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            return self.dp_opt(nums) # 7_dynamic_programming
        # return self.rec_opt(len(nums)-1,nums) # 递归

    def rec_opt(self,n,nums):
        if n==0:
            return nums[0]
        elif n==1:
            return max(nums[0],nums[1])
        else:
            A = self.rec_opt(n-2,nums)+nums[n]
            B = self.rec_opt(n-1,nums)
            return max(A,B)


    def dp_opt(self,nums):
        # dp = np.zeros(len(nums),dtype=int)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for n in range(2,len(nums)):
            # 这个n的含义还是不太懂
            # opt(n),n包含两种情况——选或者不选，
            # 代表到第n步的时候，所有的最优解
            A = dp[n-2]+nums[n] # 选这家
            B = dp[n-1] # 不选这家
            dp[n] = max(A,B)
        print(dp)
        return dp[len(nums)-1]


if __name__ == '__main__':
    nums = [2,7,9,3,1]
    print(Solution().rob(nums))