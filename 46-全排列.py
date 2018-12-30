class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        self.perm(nums,0,n)

    def perm(self, nums, p, q):
        if p == q:
            print(nums)
        for i in range(p, q):
            # for i in range(p, q+1): 这里一直报错
            # 遍历一个数组就是range(0, len(arr))
            # 你第一次调用 传入的q是len(n)，你要遍历数组 就range(0, q)就行，为啥还要+1？
            nums[p], nums[i] = nums[i], nums[p]
            # nums[p]=nums[i]
            self.perm(nums, p+1, q)
            nums[p], nums[i] = nums[i], nums[p]





if __name__ == '__main__':
    nums = [1,2,3]
    myResult = Solution()
    print(myResult.permute(nums))