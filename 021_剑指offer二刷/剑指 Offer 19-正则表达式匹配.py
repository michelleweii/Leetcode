"""
hard 二维dp
2021-07-15
dp[i][j] s的前i和字母和p的前j个字母能够匹配
dp[i][j] 代表 A 的前 i 个和 B 的前 j 个能否匹配
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/zhu-xing-xiang-xi-jiang-jie-you-qian-ru-shen-by-je/
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = True
        for i in range(len(s)+1):
            for j in range(len(p)+1):

                # 非空正则分为两种情况 * 和 非*

                # 当b[i]为.




if __name__ == '__main__':
    s = "aa"
    p = "a"
    print(Solution().isMatch(s, p))