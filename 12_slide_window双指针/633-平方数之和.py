# 双指针
class Solution:
    def judgeSquareSum(self, c):
        d = {}
        for i in range(0,int(c**0.5)+1):
            d[i * i] = 1
            if c - i*i in d:
                return True
        return False

if __name__ == '__main__':
    c = 4
    ans = Solution()
    print(ans.judgeSquareSum(c))