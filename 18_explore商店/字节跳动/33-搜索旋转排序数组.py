"""
middle 2022-02-24 二分
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/leetcode-33-sou-suo-xuan-zhuan-pai-xu-sh-ga4b/
"""
# 以nums[-1]作为二分分割点，前一半都大于它，后一半都小于它

class Solution:
    def search(self, nums, target):
        return self.bisearch(0,len(nums)-1,nums,target)

    def bisearch(self, l, r, nums, target):
        while l<r:
            mid = (l+r+1)//2
            if nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid
            elif nums[mid]==target:
                return mid
        return l if nums[l]==target else -1

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))