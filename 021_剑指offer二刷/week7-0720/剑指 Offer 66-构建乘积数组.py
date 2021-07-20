"""
middle 双向遍历
2021-07-20
"""
class Solution:
    def constructArr(self, a):
        if not a:return a
        p = 1
        b = [1 for _ in range(len(a))]
        for i in range(len(a)):
            b[i] = p
            p *= a[i]
        # print(b)
        p = 1
        for j in range(len(a)-1, -1, -1):
            # print(j)
            b[j] *= p
            p *= a[j]
        # print(b)
        return b



if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(Solution().constructArr(a))