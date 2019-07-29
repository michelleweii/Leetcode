# 度小满面试题 0513
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # print(dp) # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

        # for _ in range(m + 1): dp[0][_] = _
        # for _ in range(n + 1): dp[_][0] = _
        for a in range(m+1):dp[0][a]=a
        for b in range(n+1):dp[b][0]=b
        # print(dp) # [[0, 1, 2, 3, 4, 5], [1, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0]]

        for i in range(1, m + 1): # word1的个数
            for j in range(1, n + 1): # word2的个数
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = 1 + min(dp[j - 1][i], dp[j][i - 1], dp[j - 1][i - 1])
        return dp[n][m]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
