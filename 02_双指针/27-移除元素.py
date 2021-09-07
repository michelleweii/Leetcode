"""
easy 2021-09-06
双指针 如果等于目标值就跳过，不等于目标值则插入。
https://leetcode-cn.com/problems/remove-element/solution/shua-chuan-lc-shuang-bai-shuang-zhi-zhen-mzt8/
"""
# idx指向待插入位置，idx=0；
# x当前元素
# x==val, continue
# x!=val, 将x插入idx位置
class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        if not n:return 0
        idx = 0
        for x in nums:
            if x!=val:
                nums[idx] = x
                idx+=1
        print(nums)
        return idx


if __name__ == '__main__':
    # nums = [0,1,2,2,3,0,4,2]
    # val = 2
    nums = [3, 2, 2, 3]
    val = 3
    myResult = Solution()
    print(myResult.removeElement(nums,val))

