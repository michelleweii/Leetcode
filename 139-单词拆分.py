class Solution:
    def wordBreak(self, s, wordDict):
        if s == '':
                return True
        if len(wordDict) == 1:
            if s == wordDict[0]:
                return True
            else:
                return False

        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        for i in range(len(s)):
            temp = s[:i+1]
            for j in range(i+1):
                if temp in wordDict and dp[j]:
                    dp[i+1] = 1
                temp = temp[1:]
                # if i==7:
                #     print(j,temp)
                # print(i,j)
        return dp[len(s)] == 1



if __name__ == '__main__':
    s = "leetcode"
    # print(s[:4])
    # print(len(s))
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))
