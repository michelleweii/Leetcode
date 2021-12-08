"""
middle 2021-12-09
拓扑排序
"""
"""
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序
拓扑排序也可以通过BFS完成。
"""
class Solution:
    def findOrder(self, numCourses, prerequisites):
        pass

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().findOrder(numCourses, prerequisites))

