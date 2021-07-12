"""
middle
双指针同向
# 思路，dict中字符串的字符必须要含在s里。
# 题目要求 字典顺序最小，划重点。
ij分别指向2个字符串
while循环使用双指针，比较字符串s是否包含当前第i个dictionary中的字符串，
如果包含，则d_ptr遍历到dictionary中第i个的字符串的末尾，即d_ptr == ds_len - 1，返回dictionary[i]即为答案，即返回长度最长且字典序最小的字符串。
如果不包含，则d_ptr未遍历到dictionary中第i个的字符串的末尾，且s_ptr遍历到字符串s的末尾

"""
class Solution:
    def findLongestWord(self, s, dictionary):
        ## 用好python内置函数sort()、find(),比双指针效率更高
        ## 可以用元组表示多关键字排序，第一关键字是长度降序，第二关键字是字符串本身字典序
        dictionary.sort(key=lambda x: (-len(x), x))
        print(dictionary) # ['a', 'b', 'c']

        for x in dictionary:
            j = 0 # x
            for i in range(len(s)):
                if j >= len(x):
                    return x
                if s[i] == x[j]:
                    j += 1

            # "aaa"
            # ["aaa", "aa", "a"]
            # "aaa"
            if j == len(x): # 考虑s=aaa,d=aaa的情况
                return x
        return ""


if __name__ == '__main__':
    # s = "abpcplea"
    # dictionary = ["a", "c", "b"]
    s = "aaa"
    dictionary = ["aaa", "aa", "a"]
    print(Solution().findLongestWord(s, dictionary))