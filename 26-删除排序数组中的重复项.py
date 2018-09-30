class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        print(length)
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1]:
                length-=1
                nums.remove(nums[i])
            else:
                continue
        # print(nums)
        return length



def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    myResult = Solution()
    print(myResult.removeDuplicates(nums))

if __name__ == '__main__':
    main()