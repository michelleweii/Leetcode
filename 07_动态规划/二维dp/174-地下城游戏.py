"""
hard 2021-12-07 二维dp
https://www.bilibili.com/video/BV1X4411t7Km?spm_id_from=333.999.0.0
题目要求：从左上角顺利到达右下角，所需要的最小初始值。顺利：达到某个格子不能为0。
已知：到达右下角，需要状态=1(不能<0，又要最小)
求左上角初始值
1、求左边+上边最小的
"""
class Solution:
    def calculateMinimumHP(self, dungeon):#: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[float('inf')]*(cols+1) for _ in range(rows+1)]


if __name__ == '__main__':
    dungeon = [[-2,-3,3],
                [-5,-10,1],
                [10,30,-5]]
    print(Solution().calculateMinimumHP(dungeon))
    print(float('inf')) # inf
