class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1 5 8 (4) [7 6 (5) 3 1]
        # 1 5 8 (5) [7 6 (4) 3 1]
        # 1 5 8 5 [1 3 4 6 7] reverse
        # 从前向后找存在问题，ac都是从后向前找的
        n = len(nums)
        idx = 0
        flag = 0
        for i in range(n-1,0,-1):
            if nums[i-1]<nums[i]:
                idx = i-1
                flag = 1
                break
        # 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
        if not flag:
            nums.reverse()
            return nums
        for i in range(n-1,0,-1):
            if nums[i]>nums[idx]:
                # 找到第一个大于idx位置的数就可以交换了
                nums[idx], nums[i] = nums[i], nums[idx]
                last = nums[idx+1:]
                last.reverse()
                nums[idx+1:] = last
                return nums

if __name__ == '__main__':
    # nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    # nums = [1,2,3]
    nums = [1,3,2]
    # nums = [1,2]
    # nums = [1]
    print(Solution().nextPermutation(nums))
