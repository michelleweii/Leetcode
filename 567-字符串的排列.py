# 438. 找到字符串中所有字母异位词（异曲同工！！）
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        



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






def main():
    s1 = "hello"
    s2 = "ooolleoooleh"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.checkInclusion(s1, s2))

if __name__ == '__main__':
    main()
