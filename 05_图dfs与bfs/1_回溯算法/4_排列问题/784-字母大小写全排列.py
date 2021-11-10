from string import ascii_lowercase

class Solution(object):
    def letterCasePermutation(self, S):
        rs = [S]
        def flip(ch):
            if ch in ascii_lowercase:
                return ch.upper()
            else:
                return ch.lower()
            # one line
            # return ch.upper() if ch in ascii_lowercase else ch.lower()

        for i in range(len(S)):
            if S[i].lower() not in ascii_lowercase: # 说明当前字母是数字
                continue
            else:
                ans = []
                for cur_s in rs:
                    # print(i,cur_s)
                    tmp = cur_s[:i]+flip(cur_s[i])+cur_s[i+1:]
                    ans.append(tmp)
                rs+=ans
                # print(rs)
                # ['1ab2', '1Ab2']
                # ['1ab2', '1Ab2', '1aB2', '1AB2']
        return rs

if __name__ == '__main__':
    S = "1ab2"
    # 第一个字符串的排列之一是第二个字符串的子串
    print(Solution().letterCasePermutation(S))