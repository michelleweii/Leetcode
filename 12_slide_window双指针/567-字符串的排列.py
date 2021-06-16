"""
middle
滑动窗口 （与76+438.找到字符串中所有字母异位词相似）
"""


from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        d1, d2 = Counter(s1), Counter(s2[:len(s1)])
        for start in range(len(s1), len(s2)):
            if d1 == d2: return True
            d2[s2[start]] += 1
            d2[s2[start - len(s1)]] -= 1
            print(d2)
            if d2[s2[start - len(s1)]] == 0:
                # print(start) # 2 3 4
                del d2[s2[start - len(s1)]]
        return d1 == d2


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.checkInclusion(s1, s2))