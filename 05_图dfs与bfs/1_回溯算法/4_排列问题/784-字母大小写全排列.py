"""
middle 2021-01-17 dfs-排列问题
【模板答案】https://leetcode-cn.com/problems/letter-case-permutation/solution/java-hui-su-by-lin_xia-ulsz/
"""

from string import ascii_lowercase
class Solution(object):
    ######## 模板 ##############
    def muban_dfs(self, s):
        if s.isdigit():return s # 如果是纯数字则直接return
        self.path, self.res = [],[]
        self.backtrace(s, 0)
        return self.res

    def backtrace(self, s, start_index):
        # 回溯出口
        if len(self.path)==len(s):
            self.res.append(''.join(self.path))
            return

        ch = s[start_index]
        self.path.append(ch)
        self.backtrace(s, start_index+1)
        self.path.pop()

        # 判断是否是字符，如果是，则转换大小写
        if not ch.isdigit():
            pass



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
    # print(Solution().letterCasePermutation(S))
    a = '12'
    print(a.isdigit()) # True