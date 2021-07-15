
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
