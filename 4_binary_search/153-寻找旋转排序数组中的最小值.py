# mid < right 表面右边有序 否则左边有序 那么mid > right 则表明最小数肯定在mid 和 right之间
class Solution:
    def findMin(self, nums):
        low, high = 0, len(nums)
        while low < high - 1:
            mid = (low+high)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[low] > nums[mid-1]:
                high = mid
            else:
                low = mid
        return nums[0]


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(Solution().findMin(nums))
