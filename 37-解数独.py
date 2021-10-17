"""
hard 2021-10-17【回溯法】
1、排除已有元素
2、回溯所有可能
方块索引 = （行/3）*3 +列/3
填写（i，j）需要判断第i行有无这个元素；第j列有无这个元素；方块index里有无这个元素
row[1][2] = 1，表示第1行中2已经被使用


https://leetcode-cn.com/problems/sudoku-solver/solution/37-jie-shu-du-hui-su-sou-suo-suan-fa-xiang-jie-by-/
https://www.bilibili.com/video/BV1a4411k72j?spm_id_from=333.999.0.0
https://blog.csdn.net/qq_28410301/article/details/100560593
"""

class Solution:
    def solveSudoku(self, board):

        # 初始化row、col、index[][]
        # 该位置已有元素，置1
        # 注意1-9，映射为0-8，num-1
        for n in
        for i in range(len(board[0]))
        for i in range(len(board[0])):
            for j in range(len(board)):
                # 数独部分空格内已填入了数字，空白格用 '.' 表示。
                # 没有数据则不能初始化，跳过
                if board[i][j]=='.':continue
                index = (i//3)*3+j//3
                num = int(board[i][j])
                row[i][num-1] = 1
                col[j][num-1] = 1
                block[index][num-1]=1

    def recall(self,board,i,j):






if __name__ == '__main__':
    board =
