"""
middle
双指针反向
"""
class Solution:
    def judgeSquareSum(self, c):
        left, right = 0, int(c**0.5)
        # print(left, right, c**0.5) # 0 2 2.23606797749979
        while left <= right: # 注意这里是<=，因为c = 4返回ture
            sumof = right*right+left*left
            if sumof > c:right -= 1
            elif sumof < c: left+=1
            else: return True
        return False


        # d = {}
        # for i in range(0,int(c**0.5)+1):
        #     d[i * i] = 1
        #     if c - i*i in d:
        #         return True
        # return False

if __name__ == '__main__':
    c = 5
    ans = Solution()
    print(ans.judgeSquareSum(c))