class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        d = {}
        for i in range(0,int(c**0.5)+1):
            d[i * i] = 1
            if c - i*i in d:
                return True
        return False
"""
class Solution(object):
    def judgeSquareSum(self, c):
        clist = []  # 用列表超出时间限制，所以用字典比用列表快
        # a = round(pow(c,0.5)) # 下取整
        # a = math.ceil(a) # 上取整
        num = int(c**0.5)
        # print(num)
        for i in range(num+1):
            # print(clist)
            if i*i not in clist:
                clist.append(i * i)
            # print(c-i*i)
            if c-i*i in clist:
                return True
        return False
"""

if __name__ == '__main__':
    c = 4
    ans = Solution()
    print(ans.judgeSquareSum(c))