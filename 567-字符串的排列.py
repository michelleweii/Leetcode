# # 438. 找到字符串中所有字母异位词（异曲同工！！）
# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         # s1_num = []
#         # for i in s1:
#         #     i =  ord(i)-ord('a')
#         #     s1_num.append(i)
#         # print(s1_num)
#         #
#         # s2_num = []
#         # for i in s2:
#         #     i = ord(i)-ord('a')
#         #     s2_num.append(i)
#         # print(s2_num)
#         #
#         #
#         # lens1 = len(s1)
#         # for i in range(len(s2)):
#         #     if sum(s1_num) == sum(s2_num[i:i+lens1]):
#         #         return True
#         # return False
# class Solution(object):
    # def checkInclusion(self, s1, s2):
    #     A = [ord(x) - ord('a') for x in s1]
    #     print(A) # [0, 1, 3]
    #     B = [ord(x) - ord('a') for x in s2]
    #     print(B) # [2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]
    #
    #     target = [0] * 26
    #     for x in A:
    #         target[x] += 1
    #     print(target)
    #     # abd [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #
    #     window = [0] * 26
    #     for i, x in enumerate(B):
    #         window[x] += 1
    #         if i >= len(A):
    #             window[B[i - len(A)]] -= 1
    #             print("start")
    #             print(window)
    #         if window == target:
    #             return True
    #     # print(window)
    #     return False

from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
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



def main():
    s1 = "ab"
    s2 = "eidbaooo"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.checkInclusion(s1, s2))

if __name__ == '__main__':
    main()

# def checkInclusion(self, s1, s2):
#     """
#     :type s1: str
#     :type s2: str
#     :rtype: bool
#     """
#     # 变成s1中的字母排列组合个数了。。。我的思路
#     # 只要保证s1中的各个字母个数在s2的子串中相同即可
#     c = list(set(s1))
#     # 还要判断在s2中是否是连在一起的——判断是子串。
#     sub_s2 = ""
#     for i in range(len(s2)):
#         if s2[i] in c:
#             sub_s2 = s2[i:i+len(s1)]
#             # 用字典统计
#                 return True
#     return False
