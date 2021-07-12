# 要求时间复杂度O(N)
# https://www.bilibili.com/video/BV1Lb411w74Y
# Python solution using hash
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

        # 2021-05
        hash_map = {}
        for idx, value in enumerate(nums):
            diff = target-value
            if diff in hash_map:
                return [hash_map[diff], idx]
            hash_map[value] = idx
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums,target))