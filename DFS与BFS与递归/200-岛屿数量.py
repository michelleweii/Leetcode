from collections import deque
class Solution:
    # directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # def numIslands(self, grid):
    #     m = len(grid)
    #     # 特判
    #     if m == 0:
    #         return 0
    #     n = len(grid[0])
    #     marked = [[False for _ in range(n)] for _ in range(m)]
    #     count = 0
    #     # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
    #     for i in range(m):
    #         for j in range(n):
    #             # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
    #             if not marked[i][j] and grid[i][j] == '1':
    #                 # count 可以理解为连通分量，你可以在广度优先遍历完成以后，再计数，
    #                 # 即这行代码放在【位置 1】也是可以的
    #                 count += 1
    #                 queue = deque()
    #                 queue.append((i, j))
    #                 # 注意：这里要标记上已经访问过
    #                 marked[i][j] = True
    #                 while queue:
    #                     cur_x, cur_y = queue.popleft()
    #                     # 得到 4 个方向的坐标
    #                     dx = [-1, 0, 1, 0]
    #                     dy = [0, 1, 0, -1]
    #                     for z in range(4):
    #                         new_i = cur_x + dx[z]
    #                         new_j = cur_y + dy[z]
    #                         # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
    #                         if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][
    #                             new_j] == '1':
    #                             queue.append((new_i, new_j))
    #                             # 【特别注意】在放入队列以后，要马上标记成已经访问过，语义也是十分清楚的：反正只要进入了队列，你迟早都会遍历到它
    #                             # 而不是在出队列的时候再标记
    #                             # 【特别注意】如果是出队列的时候再标记，会造成很多重复的结点进入队列，造成重复的操作，这句话如果你没有写对地方，代码会严重超时的
    #                             marked[new_i][new_j] = True
    #                 # 【位置 1】
    #     return count


    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        res = 0
        queue = []
        m, n = len(grid), len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        print(m,n)
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j]=='1':
                    res+=1
                    queue.append((i,j))
                    marked[i][j] = True
                    while queue:
                        a,b = queue.pop(0)
                        dx = [-1,0,1,0]
                        dy = [0,1,0,-1]
                        for z in range(4):
                            x = a+dx[z]
                            y = b+dy[z]
                            # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
                            if m>x>=0 and n>y>=0 and not marked[x][y] and grid[x][y]=='1':
                                queue.append((x,y))
                                marked[x][y] = True
        return res


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '1']]
    grid = [["1", "0"]]
    print(Solution().numIslands(grid))
