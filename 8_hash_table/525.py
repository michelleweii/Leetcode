"""
560: 记录总共有几个序列 hash记录前缀和出现多少次
525: 求最长子段的长度 hash记录前缀和的下标,记录最早出现的位置
"""
# 从0到i-1里，前缀和有没有一个等于当前前缀和的相反数，如果有的话，
# 找一下离的最远的前缀和在哪，所以记录的是下标。
#
class Solution:
    def findMaxLength(self, nums):
        hash_map = {}
        hash_map[0] = -1
        s = 0 # 从0-i的前缀和
        res = 0
        for i in range(len(nums)):
            s = s+nums[i] if nums[i]==1 else -1
            if not hash_map:

            else:
                res = max(res, i-hash_map[s])

        return res



if __name__ == '__main__':
    nums =  [0,1,0]
    res = Solution()
    print(res.findMaxLength(nums))