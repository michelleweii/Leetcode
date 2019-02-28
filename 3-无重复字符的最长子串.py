class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i]是以第i个字符为开始的最长子串
        dp = [0 for _ in range(len(s))]
        dp[0]=1
        rs=s[0]
        # print(rs)
        n = len(s)
        for i in range(1,len(s)):
            for j in range(i,n,1):



if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))