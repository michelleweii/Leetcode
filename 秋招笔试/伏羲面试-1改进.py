def fn(n, m, matrix):
    cnt = 0
    res = []
    if not n or not m:return cnt
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = []
    queue.append([0,0])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        tmp = queue[0]
        queue.pop(0)
        if matrix[tmp[0]][tmp[1]]==1 or visited[tmp[0]][tmp[1]]:continue
        cnt+=1
        visited[tmp[0]][tmp[1]]=True
        for i in range(4):
            x = tmp[0]+dx[i]
            y = tmp[0]+dy[i]
            if x>=0 and x<n and y>=0 and y<m:
                queue.append([x,y])

        res.append(cnt)
    return res

if __name__ == '__main__':
    n, m = 3, 3
    matrix = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    res = fn(n, m, matrix)
    print(res)
    # for i in range(n):
    #     tmp = [str(x) for x in res[i]]
    #     print(" ".join(tmp))


# 我的做法返回的是
# 4 4 4
# 0 4 0
# 0 0 0
# 不能找到最小的
"""
给定一个由0、1数字组成的矩阵，输出同大小的矩阵，输出矩阵的每一个元素是原矩阵对应元素离数字0的最近距离。

输入描述
输入矩阵行数r，列数c，以及0,1数字组成的矩阵
输出描述
与输入矩阵相同维度的矩阵
示例1
输入
3 3
1 1 1
0 1 0
0 0 0

输出
1 2 1
0 1 0
0 0 0
"""