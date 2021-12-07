"""
hard 2021-12-08
dp
"""
class Solution(object):
    def isMatch(self, s, p):
        import re
        # re.match(pattern, string, flags=0)
        # pattern	匹配的正则表达式
        # string	要匹配的字符串（长的）
        # re.I不区分大小写
        match = re.match(p, s, re.I)
        # 匹配成功re.match方法返回一个匹配的对象，否则返回None。
        #
        # 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
        print(match) # <_sre.SRE_Match object; span=(0, 1), match='a'>
        print(match.group())  # a
        if match is not None:
            return match.group() == s
        elif match is None:
            return s == None
        else:
            return False


if __name__ == '__main__':
    s = "aabd"
    p = "a"
    print(Solution().isMatch(s,p))