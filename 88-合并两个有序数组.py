class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:m+n]=nums2[:n]
        # nums1.sort()
        # return nums1
        # 比nums1当前元素大的都向后添加，比当前小的，当前向后移动
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)


def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    myResult = Solution()
    print(myResult.merge(nums1, m, nums2, n))

if __name__ == '__main__':
    main()