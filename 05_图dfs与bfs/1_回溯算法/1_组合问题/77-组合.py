"""
回溯法——组合问题（middle）
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 没有剪枝
"""
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combine(self, n, k):
        if not k:return self.res
        self.dfs(n,k,1)
        return self.res

    def dfs(self, n, k, start_index):
        # dfs出口
        if len(self.path)==k:
            self.res.append(self.path[:])
            # return # return加不加都不影响结果，所以作用是什么？
        # 横向遍历
        for i in range(start_index, n+1):
            # 剪枝?
            self.path.append(i)
            self.dfs(n,k,i+1) # 深度遍历
            self.path.pop() # 回溯，上一级


if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().combine(n,k))