# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
"""
思路：
2个哈希表
1-左端点所代表的区间的长度。
2-右端点对代表的hash表长度。
区间内部hash值是没有用的。所求的是最长的长度。
计算当前数的区间长度为：cur_length = left + right + 1
"""
class Solution:
    def longestConsecutive(self, nums):
        res = 0
        left_hash_map = {}
        right_hash_map = {}
        for x in nums:
            left = right_hash_map.get(x-1,0) # x左边的点，它向左维护的长度
            right = left_hash_map.get(x+1,0) # x右边的点，它向右维度的长度

            # 区间更新, 因x的加入，导致区间可能的合并
            left_hash_map[x-left] = max(left_hash_map.get(x-left,0), left+1+right)
            right_hash_map[x+right] = max(right_hash_map.get(x+right,0), left+1+right)

            res = max(res, left+1+right)

        return res





if __name__ == '__main__':
    # nums = [100, 4, 200, 1, 3, 2] # 4
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] # 9
    res = Solution()
    print(res.longestConsecutive(nums))