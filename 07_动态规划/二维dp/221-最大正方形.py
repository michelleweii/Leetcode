"""
middle 2021-12-13 二维dp
题目：在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
定义：用dp(i,j)表示以(i,j)为右下角，且只包含 1 的正方形的边长最大值。

核心：若某格子值为 1，则以此为右下角的正方形的、最大边长为：上面的正方形、左面的正方形或左上的正方形中，最小的那个，再加上此格。
https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/
"""
class Solution:
    def maximalSquare(self, matrix): #List[List[str]]) -> int:
        if not matrix or not matrix[0]:return 0
        m = len(matrix)
        n = len(matrix[0])
        # dp[i][j] 以 matrix[i][j] 为右下角的正方形的最大边长
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0

        for i in range(0, m):
            for j in range(0, n):
                # //base case
                # 初始化边界值
                if (i == 0 or j == 0):
                    dp[i][j] = int(matrix[i][j])

                if matrix[i][j]=='1':
                    # 状态方程为什么这样呢？具体看链接里的图
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    max_side = max(max_side, dp[i][j]) # 记录最大边

        return max_side*max_side

if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    print(Solution().maximalSquare(matrix))