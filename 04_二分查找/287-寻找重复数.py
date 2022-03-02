"""
middle 2022-03-02 二分
[二分](https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/)
要求空间复杂度O(1)，所以不能使用哈希表。
重点理解：这个问题使用「二分查找」是在数组 [1, 2,.., n] 中查找一个整数，而 并非在输入数组数组中查找一个整数。
二分查找的思路是先猜一个数（有效范围 [left..right] 里位于中间的数 mid），然后统计原始数组中 小于等于 mid 的元素的个数 cnt：
[快慢指针](https://leetcode-cn.com/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/)
"""
class Solution:
    def findDuplicate(self, nums):
        l = 1
        r = len(nums)-1
        while l<r:
            # 找到对什么二分：统计原始数组中 <= mid 的元素的个数 cnt
            mid = l+r>>1
            sum = 0
            for x in nums:
                if x>=1 and x<=mid:sum+=1
            # 如果遍历一遍输入数组，统计小于 等于 4 的元素的个数，
            # 如果小于等于 4 的元素的个数 严格 大于 4 ，说明重复的元素一定出现在整数区间 [1..4]
            # 根据抽屉原理，小于等于 4 的个数如果严格大于 4 个，此时重复元素一定出现在 [1..4] 区间里
            if sum>mid:
                # 重复元素位于区间 [left..mid]
                r=mid
            else:
                l=mid+1
        return r

if __name__ == '__main__':
    nums = [1,3,4,2,2] # 2
    print(Solution().findDuplicate(nums))
