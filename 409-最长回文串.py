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