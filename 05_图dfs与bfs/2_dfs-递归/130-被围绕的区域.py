class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])  # m行，n列
        for i in range(m):
            for j in range(n):
                if (i == 0) or (j == 0) or (i=m-1) or (j=n-1):
                    self.dfs(board, i, j, m, n)
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'O'):
                    board[i][j] = 'X'
                elif (board[i][j] == 'M'):
                    board[i][j] = 'O'

        def dfs(self, board, i, j, m, n):
            if i < 0 or j < 0 or i > m-1 or j > n-1：
                return
            if(board[i][j] != 'O'): return
            board[i][j] = 'M'
            dfs(board, i+1, j, m, n)
            dfs(board, i, j+1, m, n)
            dfs(board, i-1, j, m, n)
            dfs(board, i, j-1, m, n)

        # print(board[0]) # ['X', 'X', 'X', 'X']
        # print('XO'[0])  # X , it is amazing!!!
        """
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
        等于, 一个二维数组
        for row in board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c == 'S']
        """


if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print(Solution().solve(board))
