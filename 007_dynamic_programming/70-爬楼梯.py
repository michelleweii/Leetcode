class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归求解，但超出时间限制
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return (self.climbStairs(n-1)+self.climbStairs(n-2))

        # 动态规划求解，两个if判断是我之前没想到的，
        # 当n==1的时候，我dp[1]=2就是越界，之前没考虑到。
        if n==0:
            return 0
        if n==1:
            return 1

        dp = [0 for _ in range(n)]
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        # print(dp)
        return dp[n-1]


if __name__ == '__main__':
    n = 5
    print(Solution().climbStairs(n))