
# 使用栈
class Solution(object):
    def longestValidParentheses(self, s):
        res = 0
        stack = [(-1,'(')]
        for i, val in enumerate(s):
            # 当前加入的元素是')',且栈顶元素是'（'
            if val == ')' and stack[-1][1] == '(':
                stack.pop()
                # 当前元素的（记录位置）下标已经弹出栈时，栈顶元素的位置
                # 即为最长有效括号
                res = max(res,i-stack[-1][0])
            else:
                stack.append((i, val))
            # print(stack)
        return res

    def dpSolution(self,s):
        n = len(s)
        if n<2: return 0

        # dp[i]表示第i个位置的最长有效长度
        dp = [0]*n
        res = 0
        for i in range(1,n):
            if s[i]==')' and s[i-1]=='(':
                # 在历史匹配数上+2
                dp[i]=dp[i-2]+2

            if s[i]==')' and s[i-1]==')':
                # 当前i的对称点索引是否存在
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