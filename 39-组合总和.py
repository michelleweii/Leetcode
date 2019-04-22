# 给定一个无重复元素的数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        item = []
        candidates.sort() # 首先要排序，必不可少，记得归纳总结这里，什么时候要排序？？
        self.dfs(candidates,target,0,item,result)
        return result

    def dfs(self,candidates,target,start,item,result):
        if target==0:
            # print(item)
            result.append(item[:])
            return
        for i in range(start,len(candidates)):
            # 剪枝
            if candidates[i]>target:
                return
            self.dfs(candidates,target-candidates[i],i,item+[candidates[i]],result)


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates,target))