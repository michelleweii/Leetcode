"""
middle
动态规划
完全背包问题，并且为“考虑排列顺序的完全背包问题”，外层循环为 target ，内层循环为选择池 nums。
dp[i] 表示和为 i 的 num 组合有 dp[i] 种。
"""
# link:https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
class Solution:
    def combinationSum4(self, nums, target):
        # target为i的元素组合数量
        dp = [0] * (target+1)
        dp[0] = 1 # 当不选取任何元素时，元素之和才为 0，因此只有 1 种方案
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
            # print(i,dp)
        return dp[target]


if __name__ == '__main__':
    nums = [1,2,3]
    target = 4
    print(Solution().combinationSum4(nums, target))