# //在遍历数组是需要记录第一，第二，第三大，和最小，次小的数（负负的正）
# // 返回Math.max(max1*max2*max3,max1*min1*min2)
def maxValue(A):
    if len(A) < 3:
        return
    sum1 = 1
    sum2 = A[0]
    # print(A)
    # print(A[:3])
    # print(A[-2:])
    for i in A[:3]:
        sum1 *= i
    for i in A[-2:]:
        sum2 *= i
    sum = max(sum1, sum2)
    print(sum)


if __name__ == '__main__':
    # A = [3,4,1,-6]
    # maxValue(A)
    while True:
        s = input().split()
        A = [int(i) for i in s]
        A = sorted(A, reverse=True)
        maxValue(A)
