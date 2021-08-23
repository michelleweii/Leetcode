"""
middle 0-1背包
感觉求所有方案数基本都是dp[i] = dp[i]+dp[i-num]
求torf，dp[i] = dp[i] OR dp[i-num]
"""
# https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/

# 数学知识：
# 我们想要的 S = 正数和 - 负数和 = x - y
# 已知 x 与 y 的和是数组总和：x + y = sum
# 可以求出 x = (S + sum) / 2 = target

class Solution:
    def findTargetSumWays(self, nums, target):
        sums = sum(nums)
        if target>sums or (sums + target) % 2 == 1: return 0
        weigth = (target+sums)//2
        dp = [0]*(weigth+1)
        dp[0] = 1 # 表示只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案。
        for num in nums:
            for i in range(weigth, num-1, -1):
                dp[i] += dp[i-num] # i >= num
        return dp[weigth]

if __name__ == '__main__':
    # nums = [1, 1, 1, 1, 1]
    # s = 3
    # (sums + target) % 2 == 1: return 0 专门针对以下情况
    nums = [7, 9, 3, 8, 0, 2, 4, 8, 3, 9]
    s = 0
    # 0
    print(Solution().findTargetSumWays(nums,s))
