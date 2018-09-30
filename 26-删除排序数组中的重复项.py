class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length-1):
            if nums[i]==nums[i+1]:
                length-=1



def main():
    nums = [1,1,2]
    myResult = Solution()
    print(myResult.removeDuplicates(nums))

if __name__ == '__main__':
    main()