class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        rs = []
        strx = str(x)
        l = list(strx)
        if l[0]=='-':
            flag = 1
        tmp = l[::-1]
        for i in range(len(tmp)):
            if l[::-1][0] == 0:
                continue
            else:
                rs.append(l[i])

        print(rs)





def main():
    x = 120
    myResult = Solution()
    print(myResult.reverse(x))

if __name__ == '__main__':
    main()