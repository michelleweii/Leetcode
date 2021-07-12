"""
特点：
# 无两段性的性质，但可以用二分来做
# 二分95%应用于有两段性性质的区间，本题属于剩下的5%
思路：
由于假设左右端点的值为负无穷，所以每次在区间中找出一点，
其到右端点要么单调递减，要么存在峰值
左端点到该点要么单调递增，要么存在峰值
步骤：
我们每次找出区间中间的点，判断它与它右边的数的大小关系（也可比较与左边的数）
若nums[mid] < nums[mid+1]说明存在单调递增，则可以判断Mid右边的区间必存在峰值，
因为只有右边是单调递减才会不存在峰值
每次筛选出的是一定存在峰值的区间，不代表另一半就没有峰值哦
若nums[mid] >= nums[mid+1]，不代表右边一定没峰值，只是代表左边一定有峰值
所以为了节省时间快速找到任意一个峰值，我们把右指针 r = mid

链接：https://www.acwing.com/solution/content/7955/
"""

class Solution:
    def findPeakElement(self, nums) -> int:
        l = 0; r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[mid + 1]: # 若当前点比右边小，则峰值在右边
                l = mid + 1
            else:
                r = mid
        return r

if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    # nums = [1, 2]
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(Solution().findPeakElement(nums))
