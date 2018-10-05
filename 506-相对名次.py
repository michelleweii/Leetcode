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
        print(tmp)
        for i in tmp[::-1]: #[2,1]
            rs.append(k)
            k+=1
        award+list(map(str,rs))
        # 之前不知道怎么将数字转为字符，所以这道题就gg了

        return list(map(dict(zip(nums[::-1],award)).get,nums))





def main():
    nums = [10,3,8,9,4]
    myResult = Solution()
    print(myResult.findRelativeRanks(nums))

if __name__ == '__main__':
    main()