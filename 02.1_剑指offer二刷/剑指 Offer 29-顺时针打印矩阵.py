"""
easy
"""
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return False
        n = len(matrix)
        m = len(matrix[0])
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        d = 1
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n*m):



if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))



