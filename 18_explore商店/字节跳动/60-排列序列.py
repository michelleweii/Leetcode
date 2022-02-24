"""
2022-02-23 hard 回溯
全排列，返回第k个排列
https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
https://leetcode-cn.com/problems/permutation-sequence/solution/shou-hua-tu-jie-jing-dian-de-dfshui-su-shu-xue-gui/
"""
#### 核心思想 ####
# 所求排列 一定在叶子结点处得到，进入每一个分支，可以根据已经选定的数的个数，进而计算还未选定的数的个数，然后计算阶乘，就知道这一个分支的 叶子结点 的个数：
# 如果 k 大于这一个分支将要产生的叶子结点数，直接跳过这个分支，这个操作叫「剪枝」；
# 如果 k 小于等于这一个分支将要产生的叶子结点数，那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解。
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0: return ""
        # 给定 n 的范围是 [1, 9]，计算从 0 到 9 的阶乘
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        print('factorial', factorial)
        # 剩下的和标准全排列一样
        used = [False for _ in range(n+1)]
        nums = [str(i) for i in range(1, n+1)]
        self.res = ""
        self.path = []
        self.dfs(nums, used, 0, factorial, k)
        return self.res

    # index是选到第几个字符做首字母了，不同位置涵盖的阶乘数量不同
    # (n-1)! 是某个首字母下的所有可能叶子节点数
    def dfs(self, nums, used, index, factorial, k):
        # 选齐了，生成了一个排列
        if len(self.path)==len(nums) and k:
            k-=1
            # 出口, 正好是第k个
            if len(self.path)==len(nums) and not k:
                self.res = ''.join(self.path)
                return


        if index==len(nums):return # 应该不会走到这一步
        pass_cnt = factorial[len(nums)-1-index]



        # print(k, self.path)

        for i in range(len(nums)):
            # 直接去下一个叶子
            if pass_cnt<k:
                k -= pass_cnt
                continue
            # 使用过的元素不再使用（同一树枝上）
            if used[i]==1:
                continue

            self.path.append(nums[i])
            used[i] = 1
            self.dfs(nums,used,index+1,factorial,k)
            self.path.pop()
            used[i] = 0



    # # 普通回溯超出时间范围
    # def getPermutation_pure(self, n: int, k: int) -> str:
    #     self.res = ""
    #     self.path = []
    #     nums = [str(i) for i in range(1, n+1)]
    #     used = [0]*n
    #     self.k = k
    #     self.dfs(nums, used)
    #     return self.res
    #
    # def dfs(self, nums, used):
    #     if not self.k:
    #         return
    #
    #     if len(self.path)==len(nums) and self.k:
    #         # self.res.append(''.join(self.path[:]))
    #         # ['123', '132', '213', '231', '312', '321']
    #         self.k-=1
    #         if self.k==0:
    #             self.res = ''.join(self.path[:])
    #             return
    #     # 不会有重复的元素，不需要剪枝
    #     for i in range(len(nums)):
    #         if used[i]==1:continue
    #         self.path.append(nums[i])
    #         used[i]=1
    #         self.dfs(nums,used) # 取过的元素不能再取
    #         used[i]=0
    #         self.path.pop()

if __name__ == '__main__':
    n = 3
    k = 3
    # '213'
    print(Solution().getPermutation(n,k))