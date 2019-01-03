from string import ascii_lowercase

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
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



    def letterCasePermutation1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        print(len(res)) # 1
        for s in S:
            # print(s)
            if not s.isalpha():
                for i in range(len(res)):
                    # print(i) # 0 1 0 1 2 3
                    res[i] += s

            else:
                for i in range(len(res)):
                    # print(i) # 0 0 1
                    tmp = res[i]
                    res[i] += s.lower()
                    # print(i, res)
                    res.append(tmp + s.upper())
                    print(i, res)
        return res


def main():
    S = "1ab2"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.letterCasePermutation(S))

if __name__ == '__main__':
    main()