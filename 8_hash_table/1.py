class Solution:
    def twoSum(self, nums, target):
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
    res = Solution()
    print(res.twoSum(nums, target))