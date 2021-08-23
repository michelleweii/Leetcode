"""
middle
dfs 回溯法
"""
class Solution(object):
    def __init__(self):
        self.res = []
        self.path = []

    def permute(self, nums):
        self.dfs(nums)
        return self.res

    def dfs(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])  # 此时说明找到了一组
        for i in range(len(nums)):
            if nums[i] in self.path:  # path里已经收录的元素，直接跳过
                continue
            self.path.append(nums[i])
            self.dfs(nums)  # 递归
            self.path.pop()  # 回溯算法

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))
