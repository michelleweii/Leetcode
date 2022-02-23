"""
2022-02-23 hard 回溯
全排列，返回第k个排列
普通回溯超出时间范围
https://leetcode-cn.com/problems/permutation-sequence/solution/shou-hua-tu-jie-jing-dian-de-dfshui-su-shu-xue-gui/
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.res = ""
        self.path = []
        nums = [str(i) for i in range(1, n+1)]
        used = [0]*n
        self.k = k
        self.dfs(nums, used)
        return self.res

    def dfs(self, nums, used):
        if not self.k:
            return

        if len(self.path)==len(nums) and self.k:
            # self.res.append(''.join(self.path[:]))
            # ['123', '132', '213', '231', '312', '321']
            self.k-=1
            if self.k==0:
                self.res = ''.join(self.path[:])
                return
        # 不会有重复的元素，不需要剪枝

        for i in range(len(nums)):
            if used[i]==1:continue
            self.path.append(nums[i])
            used[i]=1
            self.dfs(nums,used) # 取过的元素不能再取
            used[i]=0
            self.path.pop()

if __name__ == '__main__':
    n = 3
    k = 3
    # '213'
    print(Solution().getPermutation(n,k))