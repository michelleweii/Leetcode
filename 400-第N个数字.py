# 这里首先分析一下位数和规律
# 个位数：1-9，一共9个,共计9个数字
# 2位数：10-99,一共90个，共计180个数字
# 3位数：100-999，一共900个，共计270个数字
# 4位数，1000-9999，一共9000个，共计36000个数字
# 以此类推，
# 这样我们就可以首先定位到是哪个数，再找到其对应的数字
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """



def main():
    n = 11
    myResult = Solution()
    print(myResult.findNthDigit(n))

if __name__ == '__main__':
    main()