# 解法：还是从首尾两边开始比较，如果匹配就移动指针继续比较。
# 当遇到不匹配的时候，删除左边的字符或者右边的字符，只要有一种能匹配就继续。
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # flag = 0
        # lists = list(s)
        # reverse_s = lists[::-1]
        # # print(reverse_s)
        # for i,val_i in enumerate(lists):
        #     if len(lists)==1:
        #         return True
        #     else:
        #         if i<len(s)/2: # 1
        #             if val_i != reverse_s[i]:
        #                 # return False
        #                 if not flag:
        #                     del lists[i]
        #                     del reverse_s[i]
        #                     flag=1
        #                 else:
        #                     return False
        #                 # print(lists)
        #                 # print(reverse_s)
        #         else:
        #             return True


def main():
    s = "abc"
    myResult = Solution()
    print(myResult.validPalindrome(s))

if __name__ == '__main__':
    main()