"""
middle 2021-01-17 dfs-排列问题

"""

from string import ascii_lowercase
class Solution(object):
    ######## 模板 ##############
    def muban_dfs(self, s):
        if s.isdigit():return s
        self.path, self.res = [],[]
        used = [0]*len(s)
        self.backtrace(s,used)
        return self.res

    def backtrace(self, s, used):
        # 回溯出口
        if len(self.path)==len(s):
            self.res.append(''.join(self.path))
            return

        for i in range(len(s)):
            if used[i]==1:continue

            if s[i].isdigit():
                used[i] = 1
                self.path.append(s[i])
                self.backtrace(s,used)
                used[i] = 0
                self.path.pop()
            else:
                used[i] = 1
                self.path.append(s[i].lower())
                self.backtrace(s,used)
                used[i] = 0
                self.path.pop()

                used[i] = 1
                self.path.append(s[i].upper())
                self.backtrace(s,used)
                used[i] = 0
                self.path.pop()



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