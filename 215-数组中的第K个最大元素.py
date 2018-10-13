class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums1 = list(set(nums))
        # 用sort实现list的降序排列
        sorted(nums1,key=lambda x:x[1])
        print(nums)
        return nums[k+1]


def main():
    nums = [3,2,1,5,6,4]
    k = 2
    myResult = Solution()
    print(myResult.findKthLargest(nums, k))

if __name__ == '__main__':
    main()

