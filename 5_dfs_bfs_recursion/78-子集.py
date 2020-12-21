class Solution(object):
    def subsets(self, nums):
        item = []
        result = [[]]
        self.generate(0, nums, item, result)
        return result

    def generate(self, i, nums, item, result):
        if i >= len(nums):
            return
        item.append(nums[i])
        result.append(item[:])
        # print(result)
        self.generate(i + 1, nums, item, result)
        item.pop()
        self.generate(i + 1, nums, item, result)

        item = []
        result = [[]]
        self.generate(0, nums, item, result)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
