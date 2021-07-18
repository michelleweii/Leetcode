"""
easy
https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
"""
def myPow(x, n: int):
    res = 1
    for i in range(1, abs(n)+1):
        res *= x
    print(res)
    if n < 0:
        res = 1 / res
    return res

if __name__ == '__main__':
    x = 2
    n = -2
    print(myPow(2,-2))