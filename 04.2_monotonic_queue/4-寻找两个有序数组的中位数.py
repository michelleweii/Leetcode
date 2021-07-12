"""
hard 有考过
"""
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m>n:
            A,B,m,n = B,A,n,m
        if n == 0:
            return -1
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


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1,nums2))



