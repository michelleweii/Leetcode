class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            if t[i] not in s:
                return False
        return True
# or
# return sorted(s)==sorted(t)

# 字符串中str.count(i),计算单个字母出现的次数
#         or
#         if len(t) != len(s):
#             return False
#         c = set(t)
#         for i in c:
#             if t.count(i) != s.count(i):
#                 return False
#         return True

def main():
    s = "aacc"
    t = "ccac"

    myResult = Solution()
    print(myResult.isAnagram(s, t))

if __name__ == '__main__':
    main()
