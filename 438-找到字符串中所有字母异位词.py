class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """



# 如何让bac判断三个元素都在abc中呢？
# 比如，bab虽然ab在abc中，但是，没有c所以也是错的。


def main():
    s = "baa"
    p = "aa"
    myResult = Solution()
    print(myResult.findAnagrams(s, p))

if __name__ == '__main__':
    main()

# 超出时间限制
# p = sorted(p)
# len_p = len(p)
# len_s = len(s)
# flag = 0
# res = []
# for i in range(len_s-len_p+1):
#     tmp = s[i:i+len_p]
#     tmp = sorted(tmp)
#     for j in range(len_p):
#         if tmp[j] != p[j]:
#             flag = 1
#             break
#     if not flag:
#         res.append(i)
#     flag=0
# return res

