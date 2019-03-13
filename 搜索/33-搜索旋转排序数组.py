class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 需找到自增区间、旋转区间
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (mid+high)//2
            if nums[mid]==target:
                return mid



if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums,target))
