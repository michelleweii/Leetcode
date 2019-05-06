# 实际上有两个约束条件，1. 0不能单独解码 2. 两位数必须在1与26之间。
# 这道题目实际上是用DP去做，仔细想的话，可以发现就是约束版的f(n) = f(n-1) + f(n-2);
# 其中如果是s[n-1]为0，f(n-1) = 0，f(n) = f(n-2)，
# 因为0无法单独解码，而f(n-2)的条件则是必须在1与26之间，否则f(n) = f(n-1)。
class Solution:
    def numDecodings(self, s):
        pass
if __name__ == "__main__":
    s = "12"
    print(Solution().numDecodings(s))
        