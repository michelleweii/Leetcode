# 我的想法：用递归（脑残）
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(1, n):
            nextS = ''
            countC = 1
            for i in range(1, len(s)+1):
                if i == len(s) or s[i] != s[i-1]:
                    nextS += str(countC) + s[i-1]
                    countC = 1
                else:
                    countC += 1
            s = nextS
        return s

def main():
    n = 4
    myResult = Solution()
    print(myResult.countAndSay(n))

if __name__ == '__main__':
    main()