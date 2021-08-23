# 最长的回文数，只要字母是偶数个时，全都可以拿来用；
# 如果字母个数是奇数时，大于1的时候，可以舍掉一个字母，只用里面的偶数个构成字符串；
# 单个字母最多可以用一个，放在字母的最中间。
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = collections.Counter(s)
        max_length = 0
        odd = 0
        for i in myDict.keys():
            if myDict[i]%2 == 0:
                # 为偶数时，直接相加
                max_length += myDict[i]
            else:
                # 当d=3的时候，可以只用2个d构成字符串
                # 如果d=1,max_length=0,odd=1
                max_length += myDict[i]-1
                odd = 1
        return (max_length+odd)


if __name__ == '__main__':
    s = "ccc"
    myResult = Solution()
    print(myResult.longestPalindrome(s))