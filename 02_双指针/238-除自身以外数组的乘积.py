"""
middle 2021-09-09 与剑指offer题目一致
双指针
------------------------------------------------------------------------------------------
思路：
原数组：       [1       2       3       4]
左部分的乘积：   1       1      1*2    1*2*3
右部分的乘积： 2*3*4    3*4      4      1
结果：        1*2*3*4  1*3*4   1*2*4  1*2*3*1
------------------------------------------------------------------------------------------
当前位置的结果就是它左部分的乘积再乘以它右部分的乘积。因此需要进行两次遍历，第一次遍历用于求左部分的乘积，
第二次遍历在求右部分的乘积的同时，再将最后的计算结果一起求出来。
"""
class Solution:
    def productExceptSelf(self, nums):
        if not nums:return nums
        p = 1
        b = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            b[i] = p
            p *= nums[i]
        # print(b)
        p = 1
        for j in range(len(nums)-1, -1, -1):
            # print(j)
            b[j] *= p
            p *= nums[j]
        # print(b)
        return b

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))