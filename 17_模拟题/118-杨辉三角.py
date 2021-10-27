"""
easy 2021-10-27
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-jian-dan-mo-ni-by-cheu-46o9/
"""
class Solution:
    def generate(self, numRows):
        if numRows==1:return [[1]]
        res = [[1]]
        for row in range(1, numRows):
            row_res = []
            row_res[row][0] = 1
            for col in range(1,row+1):
                res[row][col] = res[row - 1][col - 1] + res[row - 1][col]

            res[row][row] = 1
        return res


if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows))