# 实际上有两个约束条件，1. 0不能单独解码 2. 两位数必须在1与26之间。
# 这道题目实际上是用DP去做，仔细想的话，可以发现就是约束版的f(n) = f(n-1) + f(n-2);
# 其中如果是s[n-1]为0，f(n-1) = 0，f(n) = f(n-2)，
# 因为0无法单独解码，而f(n-2)的条件则是必须在1与26之间，否则f(n) = f(n-1)。
class Solution:
    def numDecodings(self, s):
        if s == "" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':#编码方式为2
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:#编码方式为1
                dp.append(dp[i-2])
            elif s[i-1]!='0':#编码方式为0
                dp.append(dp[i-1])
            else:
                return 0
        #print(dp[len(s)])
        return dp[len(s)]
    
if __name__ == "__main__":
    s = "12"
    print(Solution().numDecodings(s))
        
"""
s[i-2]和s[i-1] 两个字符是10----26之间但不包括10和20这两个数时，有两种编码方式，比如23------>[“BC”，“W”]，所以dp[i] = dp[i-1]+dp[i-2]

s[i-2]和s[i-1] 两个字符10或20这两个数时，有一种编码方式，比如10------>[“J”], 所以dp[i] = dp[i-2]

s[i-2]和s[i-1] 两个字符不在上述两种范围时，编码方式为零，比如27，比如01，所以dp[i] = dp[i-1
"""
