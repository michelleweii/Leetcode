"""
middle 2022-03-02 二分查找

"""
class Solution(object):
    def searchRange(self, nums, target):
        result = []
        # print(self.leftbound(nums,target))
        # print(self.rightbound(nums, target))
        result.append(self.leftbound(nums, target))
        result.append(self.rightbound(nums,target))
        return result

    def rightbound(self,nums,target):
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if target == nums[mid]:
                if mid==len(nums)-1 or nums[mid+1]>target:
                    return mid
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return -1


    def leftbound(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                if mid == 0 or target > nums[mid-1]:
                    return mid
                high = mid-1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums,target))


