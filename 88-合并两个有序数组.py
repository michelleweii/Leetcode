class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        nums1.sort()
        for i in range(len(nums1)):
            if k!=n:
                if nums1[i] == 0:
                    nums1[i] = nums2[k]
                    k+=1




def main():
    nums1 = [1] #8
    m = 1
    nums2 = []
    n = 0
    myResult = Solution()
    print(myResult.merge(nums1, m, nums2, n))

if __name__ == '__main__':
    main()