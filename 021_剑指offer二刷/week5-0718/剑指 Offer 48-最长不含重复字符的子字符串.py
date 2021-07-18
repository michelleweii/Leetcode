"""
middle 同向双指针
2021-07-18
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        i = 0
        res = -1
        for j in range(len(s)):
            if s[j] not in hashmap:hashmap[s[j]]= j
            else:
                res = max(j-i+1,res)
                i = j


if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))