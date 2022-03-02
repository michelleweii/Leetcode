"""
hard 2021-12-10回顾 美团有考过(这里考虑递归)
中位数性质：排序数组中，右边都比它大，左边都比它小——>考虑二分
将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素。
https://www.acwing.com/solution/content/50/ （递归，太难理解了！！）题解1
https://www.bilibili.com/video/BV1nC4y1a7vT 视频题解0:50

思路：
核心是找到一个分割线，分割线具有以下性质:
- 1、当数组的总长度为偶数的时候，分割线左右的数字个数总和相等；当数组的总长度为奇数的时候，分割线左数字个数比右边仅仅多 1；
- 2、分割线左边的所有元素都小于等于（不大于）分割线右边的所有元素。

因为下标是从 0 开始编号，因此编号为 i 的元素，就刚刚好前面有 i 个元素。因此，i 就是第 1 个数组分割线的右边的第 1 个元素。
"""
class Solution(object):
    # https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/he-bing-yi-hou-zhao-gui-bing-guo-cheng-zhong-zhao-/
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        # 假定A总是比B更短。m:A, n:B
        if m>n:
            A,B,m,n = B,A,n,m

        if n == 0: return -1 # 如果更长的那个数组为0，则没有答案
        # 保证分割线左边比右边多一个数
        # // m+n 为奇数，分割线要求左侧有 (m+n)/2 + 1 个元素
        # // m+n 为偶数，分割线要求左侧有 (m+n)/2     个元素
        # // 两种情况其实可以统一写作 (m+n+1)/2，表示对(m+n)/2向上取整
        # // 对整数来说，向上取整等于：(被除数 + (除数 - 1)) / 除数

        left_total = (m+n+1)//2 # 上取整可以保证——分割线左边比右边多一个数
        left, right=0, m
        # 在短的list中找到i，满足：分割线左右两边count个数一样
        # 开始二分
        while left<right:
            # // +1 向上取整避免 left + 1 = right 时可能无法继续缩小区间而陷入死循环
            i = (left+right+1)//2 # nums1分割线右边第一个数 # 【类似求mid】，我们要找mid-1
            j = left_total-i # nums2分割线右边第一个数
#           //要找最大i，使得nums1[i-1] <= nums2[j]
#           //使用对立面缩小区间
            if nums1[i-1]>nums2[j]: #
                right = i-1
            else:
                # // i满足说明[0, i-1]均不为满足条件的最大i，舍去以缩小区间
                left = i

        # //退出循环时left=right，表示最终nums1中分割线的位置
        i = left
        # //nums2中分割线的位置
        j = left_total - left

        # // 判断极端情况——nums1与nums2左右没有元素
        # i==0, 再取i-1就越界了
        nums1_left_max = 0 if i==0 else nums1[i-1] # nums1分割线左边没有元素,中值在nums2
        nums1_right_min = nums1[m] if i==m else # nums1分割线右边没有元素，中值在num1

        nums2_left_max = nums2[j] if j==0 # nums2分割线右边没有元素,中值在nums2
        nums2_right_min = if   # nums2分割线左边没有元素，中值在num1

        if (m+n)%2==0:
            v1 = max(nums1_left_max, nums2_left_max)
            v2 = min(nums1_right_min, nums2_right_min)
            return (v1+v2)/2.0
        else:
            return max(nums1_left_max, nums2_left_max)



    """
    题解中，划分数组的方法。
    中位数定义：将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素。
    """
    # 要case的场景太多
    def findMedianSortedArrays_1(self, A, B):
        m, n = len(A), len(B)
        # 假定A总是比B更短。m:A, n:B
        if m>n:
            A,B,m,n = B,A,n,m
        # 如果更长的那个数组为0，则没有答案
        if n == 0:
            return -1
        #
        imin,imax,half_len = 0,m,(m+n+1)/2
        while imin<=imax:
            i = (imin+imax)/2
            j = half_len-i
            if i < m and B[j-1]>A[i]:
                # B[i-1]<=A[i],说明A[i]太小了,那么需要增大i，增大
                # i的时候要保证不能不能超过取值范围m
                imin = i+1
            elif i > 0 and A[i-1]>B[j]:
                # 应该A[i-1]<=B[j],说i太大了
                imax = i-1
            else:
                # i is perfect
                if i==0: max_of_left=B[j-1]
                elif j==0: max_of_left=A[i-1]
                else: max_of_left=max(A[i-1],B[j-1])
                # 如果是奇数区间
                if (m+n)%2==1:return max_of_left

                if i==m: min_of_right = B[j]
                elif j==n: min_of_right=A[i]
                else: min_of_right=min(A[i],B[j])
                return (max_of_left+min_of_right)/2.0

        #     left_part | right_part
        # A[0], A[1], ..., A[i - 1] | A[i], A[i + 1], ..., A[m - 1]
        # B[0], B[1], ..., B[j - 1] | B[j], B[j + 1], ..., B[n - 1]

#     def findMedianSortedArrays(self, A, B):
#         total = len(A)+len(B)
#         # 如果是偶数
#         if total%2==0:
#             # 找到中间的左边这个数
#             left = self.finkKthNumber(nums1,0,nums2,0,total//2)
#             # 找到中间的右边这个数
#             right = self.finkKthNumber(nums1, 0, nums2, 0, (total // 2)+1)
#             return (left+right)/2
#         # 如果是奇数
#         else:
#             return self.finkKthNumber(nums1,0,nums2,0,total//2+1)
#
#     def finkKthNumber(self,nums1,i,nums2,j,k):
#         """
#         找到两个数组中第k个数
#         :param nums1:数组1
#         :param i:从第i个位置开始
#         :param nums2:数组2
#         :param j:从第j个位置开始
#         :param k:要找的那个数
#         :return:
#         """
#         # 为了方便，假定第一个数组比较短。如果第一个数组比较长的话，就和第二个数组交换一下。
#         if (len(nums1)-i) > (len(nums2)-j): return self.finkKthNumber(nums2,j,nums1,i,k)
#         # case1 处理边界，如果找第一个数，就返回两个数的最小值即可
#         if k==1:
#             # 如果第一个数组是空的
#             if len(nums1)==i: return nums2[j]
#             else: min(nums1[i],nums2[j])
#         # case2 处理边界，如果第一数组是空的，则目标是找第二数组的第k个数
#         if len(nums1)==i:return nums2[j+k-1] # 注意k是从1开始的
#         # 计算k/2的坐标是多少
#         si = i+k//2 # k/2元素的下一个位置
#         sj = j+k-k//2
#         if nums1[si - 1] > nums2[sj - 1]: # A大，B后半段不要
#             return self.finkKthNumber(nums1,i,nums2,j+k//2,k-k//2)
#         else: # A后半段不要
#             return self.finkKthNumber(nums1,si,nums2,j,k-(si-i))

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1,nums2))



