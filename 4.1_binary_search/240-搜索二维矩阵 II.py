class Solution:
    """
    2021/01/12
    本题重点是从右上角开始二分
    注意与74题的不同之处，74是z字遍历后是一个递增的序列
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        i, j = 0, len(matrix[0])-1
        while (i<len(matrix) and j>=0):
            t = matrix[i][j]
            if t == target: return True
            if t > target: j -=1
            else: i+=1
        return False



if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 3333
    solu = Solution()
    print(solu.searchMatrix(matrix, target))

