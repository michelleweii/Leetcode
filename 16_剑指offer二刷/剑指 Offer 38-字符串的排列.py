"""
middle 2021-01-07 2_dfs-递归
https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/dai-ma-sui-xiang-lu-jian-zhi-offer-38-zi-gwt6/
本题是回溯算法经典题目，求全排列+去重，这道题目和 LC47.全排列II 几乎是一样的。
"""
# 2022-01-05
class Solution:
    # ['acb', 'bca', 'cba', 'abc', 'bac', 'cab']
    def permutation(self, s: str):
        res = []
        if not s: return res
        self.dfs("", res, s)
        return list(set(res)) # set去重

    def dfs(self, path, res, s):
        # 定义dfs出口
        if s == '': res.append(path)
        # 轮流当首字母
        for i in range(len(s)):
            self.dfs(path + s[i], res, s[:i] + s[i + 1:])
        return res

    # 存在没有去重的问题
    def permutation2(self, s):
        self.res, self.path = [], []
        if not s:return self.res
        self.backbrace(s)
        return self.res

    # 回溯要求去重
    def backbrace(self, s):
        if s=='':
            # print(self.path)
            self.res.append(''.join(self.path))

        for i in range(len(s)):
            self.path.append(s[i])

            self.backbrace(s[:i]+s[i+1:])
            self.path.pop()



if __name__ == '__main__':
    s = "abc"
    print(Solution().permutation(s))
    print(Solution().permutation2(s))