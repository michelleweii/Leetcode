# 拓扑排序
class Solution:
    def findOrder(self, numCourses, prerequisites):
        if numCourses < 2:
            return [0]
        rd = [0]*numCourses
        edges = [[] for i in range(numCourses)]
        for li in prerequisites:
            for i in range(len(li)-1):
                rd[li[i]] += 1
            for i in range(1, len(li)):
                edges[li[i]].append(li[i-1])
        stack = []
        for i in range(numCourses):
            if rd[i] == 0:
                stack.append(i)
        ans = []
        while stack:
            tmp = stack.pop()
            ans.append(tmp)
            for i in range(len(edges[tmp])):
                y = edges[tmp][i]
                rd[y] -= 1
                if rd[y] == 0:
                    stack.append(y)
        if len(ans) == numCourses:
            return ans
        return []


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().findOrder(numCourses, prerequisites))

"""
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序
拓扑排序也可以通过 BFS 完成。

"""
