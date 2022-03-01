"""
middle 2022-03-02 二分
"""
class Solution:
    def findDuplicate(self, nums):
        l = 1
        r = len(nums)-1
        while l<r:
            mid = l+r>>1
            sum = 0
            for x in nums:
                if x>=1 and x<=mid:sum+=1
            if sum>mid:r=mid
            else:l=mid+1
        return r

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))
