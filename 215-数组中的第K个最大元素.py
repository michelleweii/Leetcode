class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        # 用sort实现list的降序排列
        nums1 = sorted(nums,reverse=True)
        # print(nums) [3, 2, 1, 5, 6, 4]
        # print(nums1) [6, 5, 4, 3, 2, 1]
        return nums1[k-1]


def main():
    nums = [3,2,1,5,6,4]
    k = 2
    myResult = Solution()
    print(myResult.findKthLargest(nums, k))

if __name__ == '__main__':
    main()

