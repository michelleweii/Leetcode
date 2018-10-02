# gg
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # gg
        # n = nums.count(0)
        # print(n)
        # for i in range(n):
        #     nums.remove(0)
        # nums.extend([0]*n)
        # print(nums)

        # gg
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         del nums[i]
        #         nums.append(0)
        # return nums

        # 思路三： 移动非零元素（操作次数就是非零元素的个数）
        j = 0   # 记录非零元素应该换到第几个位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


def main():
    nums = [0,1,0,3,12]
    myResult = Solution()
    print(myResult.moveZeroes(nums))

if __name__ == '__main__':
    main()