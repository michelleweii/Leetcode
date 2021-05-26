# 还是不太懂。。。
# 对于”aab”作为输入，可以这么寻找回文：
# “a”+”ab”构成的回文串
# “aa”+”b”构成的回文串
# “aab”不是回文，所以直接退出。

# 深度优先搜索遍历是沿着图的某一条分支遍历直到末端，然后回溯，再沿着另一条进行同样的遍历，
# 直到所有的顶点都被访问过为止。
class Solution(object):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    s = "aab"
    myResult = Solution()
    print(myResult.partition(s))