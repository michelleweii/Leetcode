"""
middle dfs
需要重做 2021-07-16
"""
class Solution:
    def permutation(self, s: str):
        res = []
        if not s: return res
        self.dfs("", res, s)
        return list(set(res))

    def dfs(self, path, res, s):
        # 定义dfs出口
        if s == '': res.append(path)
        # 轮流当首字母
        for i in range(len(s)):
            self.dfs(path + s[i], res, s[:i] + s[i + 1:])
        return res


if __name__ == '__main__':
    s = "abc"
    print(Solution().permutation(s))