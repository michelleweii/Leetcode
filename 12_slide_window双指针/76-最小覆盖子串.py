"""
hard
双指针同向
子串是连续的；T可能包含重复字符

如何判断S的子串包含了T中的所有字符？
- 分别统计s的子串和T中每个字符出现的次数，逐个对比（哈希表）。
- S中每个字符出现的次数>=T中该字符出现的次数
"""

from collections import Counter
# sW_count, tW_count = Counter(sW), Counter(tW) # 统计字符串里每个字符的个数

class Solution:
    def minWindow(self, s, t):
        ls = len(s)
        lt = len(t)
        if not s or not t or ls < lt:
            return ''

        min_size = ls + 1 # 初始赋值为一个不可能达到的数
        left, right = 0, 0

        start = 0
        end = ls-1

        # 对t中的字符计数
        # map = {}
        # for c in t:
        #     map[c] = map.get(c, 0)+1
        map = Counter(t)

        match = 0
        # [left, right)
        # 右指针向右扩展，遍历s，长的那个字符串
        while right < ls:
            # s[right] 右指针看见的元素
            map[s[right]] = map.get(s[right], 0)-1
            # 如果当前遇到的字符在map中出现过，则匹配数+1
            match = match+1 if map[s[right]] >= 0 else match
            # 当匹配完成时窗口左滑
            if match == left:
                # 尝试左滑窗口 对之前遇到的字符出窗口
                while map[s[left]] < 0:
                    map[s[left]] += 1
                    left += 1
                if min_size > right - left + 1:
                    min_size = right - left + 1
                    start = left
                    end = right
            right += 1
        return '' if min_size > ls else s[start:end+1]



if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print(Solution().minWindow(S, T))
