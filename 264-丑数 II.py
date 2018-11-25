# 找出第 n 个丑数
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return False
        t1 = 0
        t2 = 0
        t3 = 0
        res = [1]
        while len(res) < n:
            # 长度可以代表第几个
            res.append(min(res[t1]*2, res[t2]*3, res[t3]*5))
            print(res)
            if res[-1] == res[t1]*2:
                t1 += 1 # t1代表2所产生的丑数到第几步了
            if res[-1] == res[t2]*3:
                t2 += 1
            if res[-1] == res[t3]*5:
                t3 += 1
        return res[-1]



if __name__ == '__main__':
    n = 10
    ans = Solution()
    print(ans.nthUglyNumber(n))
