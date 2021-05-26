"""
middle
双指针[荷兰国旗问题]
"""
class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for j in range(n-1):
            for i in range(n-1-j):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]

if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    myresult = Solution()
    print(myresult.sortColors(nums))
