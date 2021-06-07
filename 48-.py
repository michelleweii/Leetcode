"""
middle 模拟题
思路：一张图先上下反转，再对角反转
"""

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # [[7,4,1],[8,5,2],[9,6,3]]
    print(Solution().rotate(matrix))