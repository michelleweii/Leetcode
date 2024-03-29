"""
middle 2019-04-01 模拟题（不属于dfs or dfs）
https://leetcode-cn.com/problems/valid-sudoku/solution/36-jiu-an-zhao-cong-zuo-wang-you-cong-shang-wang-x/
"""
class Solution:
    def isValidSudoku(self, board):
        row = [{},{},{},{},{},{},{},{},{}] # 值：1
        col = [{},{},{},{},{},{},{},{},{}]
        cell = [{},{},{},{},{},{},{},{},{}]
        n = len(board)
        for i in range(n):
            for j in range(n):
                block = 3*(i//3)+j//3 # 找单元
                num = board[i][j]
                if num != '.':
                    if num not in row[i] and num not in col[j] and num not in cell[block]:
                        row[i][num] = 1
                        col[j][num] = 1
                        cell[block][num] = 1
                    else:
                        return False
        # print(row)
        # [{'5': 1, '3': 1, '7': 1}, {'6': 1, '1': 1, '9': 1, '5': 1},
        # {'9': 1, '8': 1, '6': 1}, {'8': 1, '6': 1, '3': 1},
        # {'4': 1, '8': 1, '3': 1, '1': 1}, {'7': 1, '2': 1, '6': 1},
        # {'6': 1, '2': 1, '8': 1}, {'4': 1, '1': 1, '9': 1, '5': 1},
        # {'8': 1, '7': 1, '9': 1}]
        return True


if __name__ == '__main__':
    board=[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(board))