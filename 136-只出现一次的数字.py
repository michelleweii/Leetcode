class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = list(set(nums))
        sumtmp = 0
        for j in tmp:
            sumtmp += j*2

        return sumtmp-sum(nums)



def main():
    listA = [4,1,2,1,2]
    myResult = Solution()
    print(myResult.singleNumber(listA))

if __name__ == '__main__':
    main()