"""
middle
字符串处理+dfs-队列

# 对于”aab”作为输入，可以这么寻找回文：
# “a”+”ab”构成的回文串
# “aa”+”b”构成的回文串
# “aab”不是回文，所以直接退出。

# 深度优先搜索遍历是沿着图的某一条分支遍历直到末端，然后回溯，再沿着另一条进行同样的遍历，
# 直到所有的顶点都被访问过为止。

1、已经划分好的区间列表；
2、当前正在枚举的区间；
3、枚举到的字符串 s 的下标；
4、字符串 s；
"""
class Solution(object):
    # 2021/05/30
    def __init__(self): # 类变量
        self.res = [] # 总的结果
        self.path = [] # 以每个点开始的，当前路径结果(当前的方案)

    def partition(self, s):
        self.dfs("", 0, s) # 当前字符串，从下标0开始，样本
        return self.res

    def dfs(self, now, u, s):
        # 已经遍历完整个字符串
        # 如果已经遍历完字符串s，则递归终止。终止前判断方案是否合法：即判断当前区间是否是回文串；
        if u==len(s):
            if self.check(now):
                self.path.append(now)
                self.res.append(self.path[:]) # 注意这里python的深拷贝
                self.path.pop() # 回溯算法
            return self.res

        # 字符串 s 还没遍历完

        # 如果当前区间是回文串，则既可以在该区间添加字符，也可以将该区间保存，并开启一个新的区间；
        if self.check(now):
            self.path.append(now)
            self.dfs("", u, s)
            self.path.pop()

        # 如果当前区间不是回文串，则只能继续在该区间添加字符；
        self.dfs(now+s[u], u+1, s)

    def check(self, now):
        # 判断当前字符串是否是回文串
        if not now:return False
        for i,j in zip(range(0,len(now)), range(len(now)-1,-1,-1)):
            # print(i,j)
            if now[i]!=now[j]:
                return False
        return True

    """
    def partition(self, s):
        res = []
        self.dfs-队列(s, [], res)
        return res

    def dfs-队列(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs-队列(s[i:], path + [s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
    """

if __name__ == '__main__':
    s = "aab"
    # s = "aba"
    myResult = Solution()
    print(myResult.partition(s))
    # print(myResult.check(s))