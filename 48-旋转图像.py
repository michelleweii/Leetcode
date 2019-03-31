class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        # print(row)
        column = len(matrix[0])
        # print(column)
        B = [[0 for _ in range(row)] for _ in range(column)]
        # print(B)
        for i in range(row):
            for j in range(column - 1, -1, -1):
                # print(j)
                B[i][j] = matrix[j][row - 1 - i]

        return B



if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().rotate(matrix))