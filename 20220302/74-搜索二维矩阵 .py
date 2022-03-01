"""
middle 2022-03-02 二分
https://leetcode-cn.com/problems/search-a-2d-matrix/solution/gong-shui-san-xie-yi-ti-shuang-jie-er-fe-l0pq/
"""
class Solution:
    """
    2021/01/12
    注意这里声明时，数组的行数没有-1
    [mid//m][mid%m] 求当前一维数组中元素mid的index,对应在二维数组中的index
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n*m-1
        while (l<r):
            mid = (l+r)>>1
            if (matrix[mid//m][mid%m] >= target): r = mid
            else: l = mid+1

        # return matrix[l // m][l % m] == target
        # while退出时，l==r，两个都ac

        return matrix[r // m][r % m] == target








if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 60]]
    # matrix = []
    target = 3
    solu = Solution()
    print(solu.searchMatrix(matrix, target))