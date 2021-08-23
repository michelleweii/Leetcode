# 给定一个无重复元素的数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def combinationSum(self, candidates, target):
        candidates.sort() # 首先要排序，必不可少，记得归纳总结这里，什么时候要排序？？
        self.dfs(candidates,target,0, 0)
        return self.res

    def dfs(self,candidates, target, sums, start_index):
        if sums==target:
            self.res.append(self.path[:])
            return

        for i in range(start_index,len(candidates)):
            # 剪枝
            if sums+candidates[i]>target:
                return

            self.path.append(candidates[i])
            sums+=candidates[i]
            self.dfs(candidates,target,sums,i) # 不用i+1了，表示可以重复读取当前的数
            self.path.pop()
            sums-=candidates[i]


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates,target))
    # 输出: [[7],[2,2,3]]