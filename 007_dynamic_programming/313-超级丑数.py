# 和264的区别在于，264是给定primes的个数，求第n个丑数
# 本题事先不知道primes的个数，所以t1,t2,...tn无法确定。

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [1] # res=[]

        lenPrimes = len(primes)
        idxPrimes = [0] * lenPrimes # 类似于t1,t2,t3记录位置
        # print(idxPrimes) # [0, 0, 0, 0]
        counter = 1
        while counter < n:
            min = pow(2, 32)
            for i in range(0, lenPrimes):
                # 找出最小值
                temp = dp[idxPrimes[i]] * primes[i]
                # 求最小的值
                if temp < min:
                    min = temp

            for i in range(0, lenPrimes):
                # 更新最小值所在的位置，类似t1+=1
                # === if res[-1] == res[t1]*2:
                if min == dp[idxPrimes[i]] * primes[i]:
                    idxPrimes[i] += 1
            print(idxPrimes)
            # res.append(min(res[t1]*2, res[t2]*3, res[t3]*5))
            dp.append(min)
            counter += 1
        # print(counter-1) # 11
        # print(len(dp))# 12
        return dp[counter - 1]


if __name__ == '__main__':
    n = 12
    primes = [2,7,13,19]
    ans = Solution()
    print(ans.nthSuperUglyNumber(n,primes))
