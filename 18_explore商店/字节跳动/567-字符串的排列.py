"""
middle 2022-02-24 同向双指针|滑动窗口
（与76+438.找到字符串中所有字母异位词相似）
https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-hua-dong-chuang-k-sos8/
思路：
needcnt需要满足的字符个数(每个字符都满足其需要的个数)
curmap只记录needmap中的字符
----
题目是求s2是否包含s1的全排列，以 s1= "ABC"、s2 = "EBBACF" 为例，
s1中的ABC分别与EBB\BBA\BAC\ACF比较，ABC与BAC符合，返回True
"""
from collections import Counter
class Solution:
    # s1是短的， s2是长的
    # 问s2是否包含s1的全排列
    def checkInclusion(self, s1, s2):
        lens1, lens2 = len(s1), len(s2)
        if not s1 or not s2 or lens1>lens2:return False

        needmap = Counter(s1)
        needcnt = len(needmap)
        curmap = {} # 遍历s2，只记录needmap中的字符

        i, j = 0, 0
        # 第一个while寻找可行解，right++
        while j<lens2:
            if s2[j] in needmap:
                curmap[s2[j]] = curmap.get(s2[j],0)+1
                # print(curmap)
                # 如果所需字符个数相等
                if curmap.get(s2[j],0)==needmap.get(s2[j],0):
                    needcnt -= 1

            # 当s2当前的窗口满足长度,需要验证是否是True
            # 第二个while寻找最优解，left++
            while j-i+1==lens1:
                if needcnt==0:return True

                # 破坏了窗口性质
                if s2[i] in needmap:
                    if curmap.get(s2[i],0)==needmap.get(s2[i],0):
                        needcnt+=1
                    curmap[s2[i]] = curmap.get(s2[i], 0) - 1

                # 如果没有破坏窗口性质，左侧缩小窗口
                i += 1

            j+=1
        return False

if __name__ == '__main__':
    # s1 = "ab"
    # s2 = "eidbaooo"
    # s1 = "ABC"
    # s2 = "EBBACF"
    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.checkInclusion(s1, s2))