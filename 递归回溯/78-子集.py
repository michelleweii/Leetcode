class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # for i in range(len(nums)):

        item = []
        result = [[]]
        self.generate(0,nums,item,result)
        return result


    def generate(self,i,nums,item,result):
        if i >= len(nums):
            return
        item.append(nums[i])
        result.append(item[:])
        # print(result)
        self.generate(i + 1, nums, item, result)
        item.pop()
        self.generate(i + 1, nums, item, result)


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))