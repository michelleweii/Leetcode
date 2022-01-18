"""
middle 2021-01-19 DFS模板题
"""
class Solution:
    # 往上下左右四个方向进行DFS。
    # 需要注意的就是访问一个字母后visited标识1，
    # 当DFS调用返回后，如果还没有找完，应该让visited置0，并返回false
    def exist(self, board, word):
        if len(word) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j): 
                    # i,j是一开始遍历的位置
                    return True
        return False
    
    def dfs(self, board, word, index, x, y):
        # 递归的出口
        if not board or index == len(word):
            return True
        # 是否越界
        if x < 0 or x == len(board) or y < 0 or y == len(board[0]):
            return False
        # 不是要找的元素
        if board[x][y] != word[index]:
            return False
        # 这几句什么意思？？ 
        source = board[x][y]
        board[x][y] = '*' # 表示此位置已经访问过，‘1’也可以，访问过的元素不再访问
        # 递归变成了四个方向的递归判断 
        exist = self.dfs(board, word, index + 1, x, y + 1) or \
                self.dfs(board, word, index + 1, x, y - 1) or \
                self.dfs(board, word, index + 1, x + 1, y) or \
                self.dfs(board, word, index + 1, x - 1, y)
        board[x][y] = source  
        return exist

"""
这实际上还是一个回溯法解决的问题。例如，对于word = 'ABCCED'，
我们从第一个元素开始，首先匹配到A，然后向后面寻找。
我们规定好寻找的顺序为：⬆️,➡️,⬇️,⬅️。我们接着找B，上面越界，右边找到了。
我们接着找C，上面越界，右边找到了。我们接着找C，上面越界了，右边不对，下面找到了。
接着找E，我们发现上面访问过，不再访问。接着向右查找，发现不匹配，接着向下查找，
发现越界了，接着想做查找，OK!我们所有元素匹配成功。
"""


if __name__ == "__main__":
    board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"
    res = Solution()
    print(res.exist(board,word))
        