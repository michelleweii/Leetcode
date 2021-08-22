"""
middle
dfs-队列
"""
# 给定一个整数 n, 返回从 1 到 n 的字典顺序。
# 例如，
# 给定 n = 13，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9]
#
"""
1、如果一个数乘以十以后没有超过n，那它后面紧挨着的应该是它的十倍，比如1,10,100。 
2、如果不满足1，那就应该是直接加一，比如n为13的时候，前一个数为12，120超过了n，
那接着的应该是13。但是这里要注意如果前一个数的个位已经是9或者是它就是n了，那就不能加一了，
比如 n = 25，前一个数为19，下一个数应该为2而不是19+1=20。25的下一个也没有26了。 
3、如果不满足2，比如19后面应该接2而不是20，这时候应该将19除以10再加一，比如n=500，
399的下一个应该是4，那就是除以十，个位还是9，继续除以10，得到3，加一得到4。

将上面的过程整理成代码就可以了，循环的次数就是n，也就是总个数。
"""
class Solution:
    def lexicalOrder(self, n):
        cur = 1
        ans = []
        for i in range(n):
            ans.append(cur)
            if cur*10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur%10 == 0:
                    cur //= 10
        return ans

    def lexicalOrderDFS(self, n):
        res = []
        for i in range(1, 10):
            self.getNum(i, n, res)
        return res

    def getNum(self, i, n, res):
        """
        递归, i为以i开头, n为不大于n, res为保存结果的数组
        """
        if i <= n:
            res.append(i)
            cur = i * 10
            if cur <= n:
                for j in range(10):
                    self.getNum(cur + j, n, res)




if __name__ == '__main__':
    n = 13
    print(Solution().lexicalOrder(n))