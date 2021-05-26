"""
middle
官方：双指针
"""
class Solution:
    def nextPermutation(self, nums):
        res = []
        item = []
        self.permu(nums,item,0,res)
        # print(res)

    def permu(self, nums, item, i, result):
        if len(item)==len(nums):
            result.append(item[:])
            return
        # item.append(nums[i])
        # print(item)
        for count in range(len(nums)):
            self.permu(nums[:], item, i + 1, result)



if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().nextPermutation(nums))