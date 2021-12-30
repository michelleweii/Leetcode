"""
middle 2021-09-09 (字节、小红书、微软)
双指针同向
思路：滑动窗口区间内的值小于target,则继续扩大右边界；
区间内的值大于target,则继续移动左指针，来缩小窗口；只要一小于target就移动右指针；
需要维护min(res)，求得长度最小的子数组
"""
class Solution:
    def minSubArrayLen(self, target, nums):
        left, right = 0, 0
        n = len(nums)
        sums = 0 # 区间和
        res = n + 1 # 最小长度, 取一个不存在的数
        while right < n:
            # 还有剩余元素未考察并且窗口内元素总和<目标值target
            sums += nums[right]
            right += 1
            # 窗口内的和超过target了,left++,尝试缩小窗口
            while sums >= target:
                res = min(res, right - left) #窗口内元素总和>=目标值target则更新结果值
                sums -= nums[left]
                left += 1

        return res if res != (n+1) else 0


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(target, nums))
