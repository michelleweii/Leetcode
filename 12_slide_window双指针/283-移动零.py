"""
easy
双指针同向
# 移动非零元素（操作次数就是非零元素的个数）
# j 记录非零元素应该换到第几个位置，记录0的位置
# i 遍历数组
"""
class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                # print(i, j)
                nums[i],nums[j] = nums[j],nums[i]
                j+=1

        return nums


if __name__ == '__main__':
    nums = [1,1,0,3,12]
    myResult = Solution()
    print(myResult.moveZeroes(nums))