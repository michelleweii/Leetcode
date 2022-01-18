"""
middle 2021-01-17 dfs-排列问题
【模板答案】https://leetcode-cn.com/problems/letter-case-permutation/solution/java-hui-su-by-lin_xia-ulsz/
"""
# dfs简答应用
# https://leetcode-cn.com/problems/letter-case-permutation/solution/dfsjian-dan-ying-yong-by-xiao-cheng-97-vk1h/
# 通过dfs遍历输入字符，对于DFS中的每一层（即操作某个字符）都有可能有两种选择：
# 1)不改变当前字符; 2)当期字符若为字母 则改变大小写状态
#

# 方法一：回溯
# https://leetcode-cn.com/problems/letter-case-permutation/solution/python-dfs-by-qinyu-c-2ln5/

# 隐藏回溯：https://leetcode-cn.com/problems/letter-case-permutation/solution/dfs-shi-jian-chao-97-by-wongdaweeee-qifq/
# 方法二：DFS
#
class Solution(object):
    def letterCasePermutation(self, s):
        if s.isdigit(): return [s]  # 如果是纯数字则直接return
        self.res, self.path = [], []
        self.backtrace(s, 0)
        return self.res

    def backtrace(self, s, idx): # idx当前s的下标
        if len(self.path) == len(s):
            self.res.append(''.join(self.path[:]))
            return # 没有return会越界

        ch = s[idx]
        if ch.isdigit():
            self.path.append(ch)
            self.backtrace(s, idx + 1)
            self.path.pop()
        else:
            self.path.append(ch.lower())
            self.backtrace(s, idx + 1)
            self.path.pop()

            self.path.append(ch.upper())
            self.backtrace(s, idx + 1)
            self.path.pop()


    ######## 模板 ##############
    # def letterCasePermutation_dfs(self, s):
    #     if s.isdigit():return s # 如果是纯数字则直接return
    #     self.res = []
    #     # s = [x for x in s]
    #     self.dfs(s, 0)
    #     return self.res

    # def dfs(self, s, cur_index):
    #     """
    #     :param s:
    #     :param cur_index: 定位s的下标
    #     :return:
    #     """
    #     # 出口
    #     if cur_index==len(s)-1:
    #         self.res = ''.join(path)
    #
    #     if cur_index>len(s)-1:return
    #     if len(self.res)==len(s):
    #         self.res.append(s)
    #         return
    #
    #     ch = s[cur_index]
    #     # 如果是数字就直接下一次递归
    #     if ch.isdigit():
    #         self.res.append(ch)
    #         self.backtrace(s, cur_index+1)
    #     # 如果是小写字母，需要将此字母递归到下一层同时也需要将此字母转换为大写再递归
    #     else:
    #         if ch >='A' and ch <= 'Z':
    #             tmp =  s[cur_index].lower()
    #             s[cur_index] = tmp
    #         elif ch >= 'a' and ch <= 'z':
    #             tmp = s[cur_index].upper()
    #             s[cur_index] = tmp
    #
    #         self.backtrace(s, cur_index+1)
    #

if __name__ == '__main__':
    S = "1ab2"
    # 第一个字符串的排列之一是第二个字符串的子串
    print(Solution().letterCasePermutation(S))
    print(Solution().letterCasePermutation_dfs(S))
    # a = '12'
    # print(a.isdigit()) # True