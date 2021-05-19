# 从后往前维护一个单调栈
# 若出现了栈顶元素比当前元素小的情况
# 说明找到了一个中间元素，大于它后面的元素
# 与此同时由于单调栈的特性我们维护的这个“后面的元素”会尽可能大，只要存在一个前面的元素比它小即可

# ai,aj,ak
class Solution:
    def find132pattern(self, nums):
        if not nums: return False
        stk = []  # 栈里维护的是aj，最大的元素
        ak = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < ak: return True  # ai找到了
            # 栈里维护最大的元素
            while stk and nums[i] > nums[stk[-1]]:
                ak = nums[stk[-1]]  # ak是被出栈的，次于item的值
                # print("s3:",ak)
                stk.pop()
            stk.append(i)
            # print("stk:",stk)
        return False


"""
还可以直接存数值
class Solution:
    def find132pattern(self, nums):
        stack = []
        _MIN = float('-inf')

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < _MIN:
                return True
            while stack and nums[i] > stack[-1]:
                _MIN = stack.pop()
            stack.append(nums[i])

        return False
"""

if __name__ == '__main__':
    # nums = [1, 2, 3, 4] #f
    nums = [3, 1, 4, 2]  # t
    res = Solution()
    print(res.find132pattern(nums))