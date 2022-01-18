"""
middle 2021-01-20 dfs
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()
https://leetcode-cn.com/problems/generate-parentheses/solution/cpython3java-1dfs-2hui-su-by-hanxin_hanx-690m/
"""
class Solution(object):
    def generateParenthesis(self, n):
        res = []
        n,m = n,0
        self.generate("",n,m,res)
        return res

    def generate(self,str,n,m,res):
        # 当前字符串，左括号个数，右括号个数，返回的结果数组
        if n==0 and m==0:
            # 括号都用完了
            res += [str]
            return res
        if n>0:
            self.generate(str+"(",n-1,m+1,res)
        if m>0:
            self.generate(str+")",n,m-1,res)

if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))