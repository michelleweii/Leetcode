"""
middle
滑动窗口+数组哈希表（与567，76相似）
---------------------------------
解题思路
（1）初始化 left = right = 0 把索引 <左闭右闭> 区间 [left, right] 当做一个 "窗口"。
（2）不断增加 right 指针扩大窗口 [left, right]，直到窗口中的字符串符长度与字符串 tt 的长度相等。
（3）此时，停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的字符串长度不再符合要求。
    同时，每增加一次 left，就要更新一轮结果。
（4）重复第 2 和第 3 步，直到 right 到达字符串 s 的尽头。
其中，第 2 步相当于在寻找一个 "可行解"，第 3 步相当于在判断这个可能的 "可行解"，最终找到 "最优解"。

flag：记录窗口中满足条件的字符个数
若一个字符进入窗口，应该增加 window 计数器；若一个字符将移出窗口，应该减少 window 计数器；当 flag 满足 pMap 时应收缩窗口；
收缩窗口的时候应该更新最终结果。

链接：https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-hua-dong-chuang-k-sos8/
"""
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        n = len(s)
        res = []
        # window 记录窗口中的字符
        window_map = {}
        p_map = Counter(p)
        left, right = 0, 0

        while right < n: # 遍历长的字符串
            window_map[s[right]] = window_map.get(s[right], 0) + 1
            while window_map.get(s[right], 0)>p_map.get(s[right], 0):
                window_map[s[left]] = window_map.get(s[left], 0) - 1
                left += 1
            if right-left+1 == len(p):
                res.append(left)
            right += 1
        return res

        # flag = 0  # 记录窗口中满足条件的字符个数
        #     if s[right] in p_map:
        #         window_map[s[right]] = window_map.get(s[right],0) + 1
        #         if window_map.get(s[right]) == p_map.get(s[right]): flag+=1 # 当flag==len(p) 说明完成匹配
        #
        #     while right-left+1 == len(p):
        #         if flag==len(p_map): res.append(left)
        #         # 开始找最优解
        #         left += 1
        #         if s[left] in p_map:
        #             if window_map.get(s[left]) == p_map.get(s[left]): flag -= 1
        #             window_map[s[left]] = window_map.get(s[left], 0) - 1
        #     right += 1
        # return res

if __name__ == '__main__':
    s = "baa"
    p = "aa"
    myResult = Solution()
    print(myResult.findAnagrams(s, p))