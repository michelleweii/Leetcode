"""
middle
[完全背包+考虑排列顺序]，外层循环为 target ，内层循环为选择池 wordDict。
dp[i] 表示以 i 结尾的字符串(包括i)是否可以被 wordDict 中组合而成。
target = s
arrs = wordDict

边界条件，我们定义 dp[0] = true 表示空串且合法。
"""
class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        # dp[i] 表示以 i 结尾的字符串是否可以被 wordDict 中组合而成
        for i in range(1, len(s)+1):
            for word in wordDict:
                word_len = len(word)
                # if i-word_len>=0:print(i, word_len, s[i-word_len: i])
                if i-word_len>=0 and s[i-word_len: i] in wordDict:
                    dp[i] = dp[i] or dp[i-word_len]
                    # print(dp)

        return dp[-1]


if __name__ == '__main__':
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    s = "dogs"
    wordDict = ["dog", "s", "gs"]
    print(Solution().wordBreak(s, wordDict))


"""
1 1 d
2 1 o
2 2 do
3 3 dog
[True, False, False, True, False]
3 1 g
3 2 og
4 3 ogs
4 1 s
[True, False, False, True, True]
4 2 gs
[True, False, False, True, False]
False
"""