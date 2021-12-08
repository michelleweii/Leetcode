"""
hard 2021-12-08
栈 or dp都可以解决
"""
class Solution(object):
    # # 栈: 存'('的下标
    # 如果是'('就直接入栈；如果是')'就开始匹配；
    # 匹配分情况讨论：
    # 1、如果栈为空，start+=1
    # 2、如果栈顶是'('，栈顶弹栈，# case 1 弹完如果栈为空()()：更新长度 res = max(res, index-start+1)
    #                       # case 2 弹完栈不为空(())：更新长度 res = max(res, index-stk.top())
    def longestValidParentheses(self, s):
        stk = []
        res = 0
        start = 0 # 记录入栈i
        for i in range(len(s)):
            if s[i]=='(': stk.append(i)
            else:
                if stk: # 如果栈不为空
                    stk.pop()
                    # case 1
                    if not stk: res = max(res, i-start+1)
                    # case 2
                    else: res = max(res, i-stk[-1])
                else: # 如果栈是空的，没办法匹配
                    start = i+1 # ")()())()()("
        return res

    # # 一维dp
    def dpSolution(self,s):
        # dp数组，其中第 i 个元素表示以下标为 i 的字符结尾的最长有效子字符串的长度
        n = len(s)
        if n<2: return 0
        dp = [0]*n
        dp[1] = 2 if s[0]=='(' and s[1]==')' else 0

        for i in range(2, n):
            # () 情况
            if s[i]==')' and s[i-1]=='(':

                dp[i] = dp[i-2] + 2 # # 在历史匹配数上+2

            #)()(())) 情况，就是(())
            if s[i]==')' and s[i-1]==')':
                # 当前i的对称点索引是否存在
                # 和s[i]配对对位置，并判断其是否是 (即可。和其配对对位置为：i−dp[i−1]−1。
                if i-dp[i-1]-1>=0:
                    if s[i-dp[i-1]-1]=='(':
                        dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
        # print(dp)
        return max(dp)


if __name__ == '__main__':
    # s = "(()"
    s = "()(()"
    # print(Solution().longestValidParentheses(s))
    print(Solution().dpSolution(s))