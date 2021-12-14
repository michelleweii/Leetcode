"""
middle 2021-12-14 二维dp
题目：求自顶向下的最小路径和， 定义dp[i][j]为从点(i,j)到底边的最小路径和
[i,j]
[i+1,j] [i+1,j+1]
https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/
"""
class Solution(object):
    def minimumTotal(self, triangle):
        m = len(triangle) # m行m列
        dp = [[0]*(m+1) for _ in range(m+1)] # (i,j)点到底边的最小路径和
        # print(dp)
        # 初始化边界
        for j in range(m):
            dp[m-1][j] = triangle[m-1][j] # 但是triangle没有index=4
        # print(dp)
        for i in range(m-2, -1, -1):
            for j in range(i, -1, -1):
                # 到达[i,j]的最短路径
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        ## 从三角形的最后一行开始递推，如下循环也ok
        # for (int i = n - 1; i >= 0; i--) {
        #     for (int j = 0; j <= i; j++) {
        return dp[0][0]

if __name__ == '__main__':
    # triangle = [[-10]]
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# [2]
# [3, 4]
# [6, 5, 7]
# [4, 1, 8, 3]
    print(Solution().minimumTotal(triangle))