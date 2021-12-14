"""
middle 2021-12-14 dp(01背包)
01 背包，即数组中的元素不可重复使用，外循环遍历 arrs，内循环遍历 target，且内循环倒序。
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
"""
# target 是什么？sum//2
# 是否可以将这个数组分割成两个子集，使得两个子集的元素和相等
# dp[i] 表示是否存在和为 i 的 组合。
class Solution:
    def canPartition(self, nums): #List[int]) -> bool:
        sum = 0
        for num in nums:
            sum+=num
        # 如果是基数就直接返回False
        if sum%2==1:return False
        target = sum//2

        dp = [False for _ in range(target+1)]
        dp[0] = True # 什么都不取

        # 【模板】外循环遍历 arrs，内循环遍历 target，且内循环倒序
        for x in nums:
            for i in range(target, x-1, -1): #i>=x
                dp[i] = dp[i] or dp[i-x] # 不选or选

        return dp[target]

if __name__ == '__main__':
    nums = [1, 2, 3, 5] # f
    print(Solution().canPartition(nums))