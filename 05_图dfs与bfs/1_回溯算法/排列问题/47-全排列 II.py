"""
middle 回溯法-排列问题-有重复元素
排列问题只要树的叶子节点，两个list可以交错插入，
所以不需要从start_index开始；
(必须要有used，因为没有start_index了，所以不可以在用i>start_index来去重)
有重复元素需要sort；
"""
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def permuteUnique(self, nums):
        if not nums:return self.res
        nums.sort()
        used = [0]*len(nums)
        self.dfs(nums,used)
        return self.res

    def dfs(self,nums,used):
        # 定义出口
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return

        for i in range(len(nums)):
            # 如果树层里重复取值，跳过
            #      // used[i - 1] == 1，说明同⼀树⽀nums[i - 1]使⽤过
            #      // used[i - 1] == 0，说明同⼀树层nums[i - 1]使⽤过
            #      // 如果同⼀树层nums[i - 1]使⽤过则直接跳过
            if i>0 and nums[i]==nums[i-1] and used[i-1]==0:  # i>0对len(nums)==1的很重要
                continue

            # 剪枝(如果当前的元素已经被用过，continue)
            # 排列问题特有的部分，因为没有start_index来标记元素是否访问
            if used[i]==1:
                continue

            self.path.append(nums[i])
            used[i] = 1
            # 树枝递归
            self.dfs(nums,used)
            self.path.pop() # 回溯
            used[i] = 0 # 回溯


if __name__ == '__main__':
    # nums = [1,1,2]
    nums = [1]
    print(Solution().permuteUnique(nums))
