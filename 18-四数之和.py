class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 先求数字的两两之和，存到一个list里。
        # 再两次for循环，将4sum转为2sum
        # 2sum时，在list中找是否存在元素。
        

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums,target))
