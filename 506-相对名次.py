# 用map
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rs = []
        nums.sort()
        award = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        k = 4

        tmp=nums[0:-3]
        for i in tmp[::-1]:
            rs.append(str(k)+
            k+=1
        return award+rs





def main():
    nums = [5, 4, 3, 2, 1]
    myResult = Solution()
    print(myResult.findRelativeRanks(nums))

if __name__ == '__main__':
    main()