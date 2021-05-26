class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                # i+=1
            else:
                i += 1
        # print(nums)
        return len(nums)

def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    myResult = Solution()
    print(myResult.removeElement(nums,val))
    # print(range(val))
    # del nums[2]
    # print(nums)

if __name__ == '__main__':
    main()

