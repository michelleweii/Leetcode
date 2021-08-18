"""
middle
是否可以用 wordDict 中的词组合成 s，完全背包问题，并且为“考虑排列顺序的完全背包问题”，外层循环为 target ，内层循环为选择池 wordDict。
dp[i] 表示以 i 结尾的字符串是否可以被 wordDict 中组合而成。
考虑顺序，外层target，内层arrs。内循环正序。
"""
# https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1) # 以i结尾的单词能不能由word所构成
        dp[0] = True # 空串
        for i in range(len(s)+1):
            for word in wordDict:
                sz = len(word)
                if i>=sz and word==s[i-sz:i]:
                    dp[i] = dp[i] or dp[i-sz]
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))
