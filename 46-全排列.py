class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.perm(nums,0,len(nums)-1)

    def perm(self, nums, p, q):
        if p == q:
            print(nums)
        for i in range(p, q+1):
            nums[p] = nums[i]
            self.perm(nums, p+1, q)
            nums[i] = nums[p]





if __name__ == '__main__':
    nums = [1,2,3]
    myResult = Solution()
    print(myResult.permute(nums))