class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return (self.climbStairs(n-1)+self.climbStairs(n-2))

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