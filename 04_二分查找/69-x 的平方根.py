"""
easy 2022-02-24 二分
【牛顿迭代法】https://leetcode-cn.com/problems/sqrtx/solution/niu-dun-die-dai-fa-by-loafer/
"""
class Solution:
    def mySqrt(self, x):
        left = 1
        right = x//2
        if(x == 0):
            return 0
        def search(l, r):
            if(int(l) >= int(r)):
                return int(l)
            mid = (l+r) / 2
            if(mid*mid>x):
                return search(l, mid)
            elif(mid*mid<x):
                return search(mid, right)
            else:
                return int(mid)
        return search(left, right)

if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))