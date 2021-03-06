class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


if __name__ == '__main__':
    numCourses = [[1, 0]]
    prerequisites = [[1, 0]]


"""
点的集合。

该方法的每一步总是输出当前无前趋（即入度为零）的顶点。为避免每次选入度为 0 的顶点时扫描整个存储空间，可设置一个队列暂存所有入度为 $0$ 的顶点。

具体做法如下：

1、在开始排序前，扫描对应的存储空间，将入度为 0 的顶点均入队列。

2、只要队列非空，就从队首取出入度为 0 的顶点，将这个顶点输出到结果集中，并且将这个顶点的所有邻接点的入度减 1，在减 1 以后，发现这个邻接点的入度为 0 ，就继续入队。
"""
