# 二分查找
class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        # 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
        return low

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))