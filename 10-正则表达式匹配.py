class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        import re
        match = re.match(p, s, re.I)
        if match is not None:
            return match.group() == s
        elif match is None:
            return s == None
        else:
            return False


if __name__ == '__main__':
    s = "aa"
    p = "a"
    print(Solution().isMatch(s,p))