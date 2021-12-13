"""
middle 2021-12-15 带权并查集dfs
"""
class Solution:
    def calcEquation(self, equations, values, queries):


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    # [3.75000,0.40000,5.00000,0.20000]
    print(Solution().calcEquation(equations,values,queries))