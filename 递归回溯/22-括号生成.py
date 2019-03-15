# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
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