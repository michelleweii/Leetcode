"""
middle 快速幂
https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
"""
class Solution:
    # 可以直接略过的题目
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(1, abs(n)+1):
            res *= x
        if n < 0:
            res = 1 / res
        return res

if __name__ == '__main__':
    x = 2.00000
    n = 10
    print(Solution().myPow(x, n))