# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = ""
        for i in s:
            if i == " ":
                res += "%20"
            else:
                res += i
        return res


if __name__ == '__main__':
    s = "We Are Happy"
    print(Solution().replaceSpace(s))
