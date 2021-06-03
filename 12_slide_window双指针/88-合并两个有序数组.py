"""
easy
双指针双向
# https://leetcode-cn.com/problems/merge-sorted-array/solution/hua-jie-suan-fa-88-he-bing-liang-ge-you-xu-shu-zu-/
难死了 easy个锤子
"""
class Solution:
    # Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        p, q = 0, 0
        while p<m and q<n:
            if nums1[p]<=nums2[q]:
                p += 1
            else:
                nums[]




if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(Solution().merge(nums1, m, nums2, n))
