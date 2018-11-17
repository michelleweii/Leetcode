class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for j in range(n-1):
            for i in range(n-1-j):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
        # print(nums)


def main():
    nums = [2, 0, 2, 1, 1, 0]
    myresult = Solution()
    print(myresult.sortColors(nums))


if __name__ == "__main__":
    main()
