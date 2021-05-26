# 判断一个数是否为丑数
class Solution(object):
    # 和求质数的思路一样
    # 每一个丑数必然是之前丑数与2，3或5的乘积得到的，这样下一个丑数就是用之前的丑数分别乘以2，3，5

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 暴力
        while num>1:
            if num%2==0:
                num = num//2
            elif num%3==0:
                num = num//3
            elif num%5==0:
                num = num//5
            else:
                break
        if num==1:
            return True
        else:
            return False

if __name__ == '__main__':
    num = 14
    ans = Solution()
    print(ans.isUgly(num))