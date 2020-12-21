# 你的解法应该是 O(logN) 时间复杂度的。
# 上坡必有坡顶，所以二分查找大的那一半一定会有峰值

# 规律一：如果nums[i] > nums[i+1]，则在i之前一定存在峰值元素
# 规律二：如果nums[i] < nums[i+1]，则在i+1之后一定存在峰值元素
"""
Conditions:
     1. array length is 1  -> return the only index 
     2. array length is 2  -> return the bigger number's index 
     3. array length is bigger than 2 -> 
           (1) find mid, compare it with its left and right neighbors  
           (2) return mid if nums[mid] greater than both neighbors
           (3) take the right half array if nums[mid] smaller than right neighbor
           (4) otherwise, take the left half
"""


class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        first, last = 0, n-1
        while first < last:
            mid = (first+last)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                first = mid+1
            else:
                last = mid-1
        return first  # cinditions 1,2


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    nums = [1, 2]
    # nums = [1, 2, 1, 3, 5, 6, 4]
    print(Solution().findPeakElement(nums))
