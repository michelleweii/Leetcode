"""
middle 2021-11-09
回溯：https://leetcode-cn.com/problems/gray-code/solution/hui-su-javadai-ma-zhu-shi-by-xiao-xiao-l-sz0r/
https://leetcode-cn.com/problems/gray-code/solution/wa-pian-89-ge-lei-bian-ma-java-zhong-ji-s3rv2/
要求：二进制两个连续的数值仅有一个位数的差异。
"""
class Solution:
    def __init__(self):
        self.res = []

    def grayCode(self, n):
        # gray编码要去必须以0开始
        if n==0:return [0]
        elif n==1:return [0,1]
        # else:
        self.back_trace(n, [], ['0','1'])
        return self.res

    def back_trace(self, n, substring, nums):
        if len(substring)==n:
            # print(substring, type(substring), "".join(substring))
            self.res.append(int("".join(substring), 2)) # int("100111",2) 2进制转10进制
            return
        # 回溯第一个状态
        substring.append(str(nums[0]))
        self.back_trace(n, substring, ['0','1'])
        substring.pop()
        # 回溯第二个状态
        substring.append(str(nums[1]))
        self.back_trace(n, substring, ['1', '0'])
        substring.pop()



if __name__ == '__main__':
    n = 3
    print(Solution().grayCode(n))