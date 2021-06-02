"""
middle
双指针扫描
思路：
定义两个指针i,j。表示当前扫描到的子串是[i,j]，
扫描过程中维护一个哈希表，表示[i,j]中每个字符出现的次数。
1、指针j向后移动一位，同时将哈希表s[j]的计数+1，hash[s[j]]++；
2、假设j移动前的区间[i,j]中没有重复字符，则 j 移动后，只有s[j]可能出现2次。
因此我们不断向后移动i，直至区间[i,j]中s[j]的个数等于1为止；
"""
class Solution(object):
    # 2021/05/30
    # 以s[j]为右端点，向左延生，最远能延生到的i的位置
    def _lengthOfLongestSubstring(self, s):
        hash_map = {}
        i = 0
        res = 0
        for j in range(len(s)):
            hash_map[s[j]] = hash_map.get(s[j],0)+1
            while hash_map[s[j]]>1:
                hash_map[s[i]] = hash_map[s[i]]-1
                i += 1
            res = max(res,j-i+1)
        return res

    def lengthOfLongestSubstring(self, s):
        hash_map = {}
        left,res = 0,0
        for i in range(len(s)): # i就是now，
            # 如果当前字符从没出现过，或者是出现了，但不包含在当前窗口内：
            if s[i] not in hash_map or hash_map[s[i]]<left:
               res = max(res,i-left+1)
            else:
                left = hash_map[s[i]]+1
            hash_map[s[i]] = i
        # print(hash_map) # {'a': 3, 'b': 4, 'c': 5}
        return res

if __name__ == '__main__':
    s = "abcabc"
    print(Solution().lengthOfLongestSubstring(s))