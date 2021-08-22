class Solution(object):
    def minimumTotal(self, triangle):
        dp = [[0 for _ in range(len(row))] for row in triangle]
        row = len(triangle)
        for j in range(row):
            dp[row-1][j] = triangle[row-1][j]
        # for row_dp in dp:
        #     print(row_dp)
        for i in range(row-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        # for row_dp in dp:
        #     print(row_dp)
        return dp[0][0]





if __name__ == '__main__':
    # triangle = [[-10]]
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # print(triangle[0][0]) # 2
    # print(triangle[2][1]) # 5
    for row in triangle:
        print(row)
# [2]
# [3, 4]
# [6, 5, 7]
# [4, 1, 8, 3]
    # print(Solution().minimumTotal(triangle))