"""
middle
双指针
# 27,26，283思路相同

"""

class Solution:
    def removeDuplicates(self, nums):
        i = 2  # 每个元素最多出现两次
        lens = len(nums)-1
        while i<lens:
            if nums[i]==nums[i-2]:
                del nums[i]
                lens -=1
            else:
                i += 1
        return len(nums)


if __name__ == "__main__":
    # nums = [1,1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    # nums = [1,1,1,1]
    res = Solution()
    print(res.removeDuplicates(nums))
