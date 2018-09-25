# -*- coding:utf-8 -*-
"""
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:

给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。

"""
class Solution(object):
    def findComplement(self, num):
        res = []
        result = 0
        # 十进制转二进制的方法：除2取余，逆序排
        res.append(str(num%2))
        while (num//2 != 0):
            num = num//2
            res.append(str(num%2))
        res.reverse() # 逆序
        print(res)
        # 按位取反
        for i,val_i in enumerate(res):
            if (val_i=='0'):
                res[i] = '1'
            else:
                res[i] = '0'
        print(res)
        # 2进制转为10进制
        for j,val_j in enumerate(res):
            if (val_j == '1'):
                result += pow(2, len(res)-1-j)
        return result

def main():
    num = 5
    myresult = Solution()
    print(myresult.findComplement(num))

if __name__ == "__main__":
    main()

