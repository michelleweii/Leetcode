class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs = []
        nums.sort()
        print(nums)
        for i in range(1,len(nums)-1,2):
            print(i)
            if nums[i-1]!=nums[i]:
                rs.append(nums[i-1])
        # print(rs)
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            rs.append(nums[len(nums)-1])
        print(rs)

        # # 超出时间限制
        # rs = []
        # dict = {}
        # for i in nums:
        #     if i not in dict.keys():
        #         dict[i] = 1
        #     else:
        #         count = dict[i]
        #         count += 1
        #         dict[i] = count
        # for key,value in dict.items():
        #     if value!=2:
        #         rs.append(key)
        #     if len(rs)==2:
        #         return rs

def main():
    nums = [1,2,1,3,2,5]
    myResult = Solution()
    print(myResult.singleNumber(nums))

if __name__ == '__main__':
    main()
