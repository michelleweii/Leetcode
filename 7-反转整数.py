from pythonds.basic.stack import Stack

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str1 = str(x).split('-')
        # print(str1)
        if len(str1)>1:
            temp = '-'+str1[1][::-1]
            if int(temp)>-2**31 and int(temp)<2**31-1:
                return int(temp)
            return 0
        else:
            if int(str1[0][::-1])>-2**31 and int(str1[0][::-1])<2**31-1:
                return int(str1[0][::-1])
            return 0




    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """

        rs = []
        pos = 0
        flag=0
        # listx = list(map(int, str(x)))
        if str(x)[0]=='-':
            flag = 1
            x = str(x)[1:]

        listx = list(map(int, str(x)))
        revlistx = listx[::-1]
        # print(revlistx)
        for i in range(len(revlistx)):
            if revlistx[i]!=0:
                pos = i
                break
        # print(pos)
        for j in range(pos,len(listx)):
            rs.append(revlistx[j])
        # print(rs)
        tmp = ''.join(list(map(str,rs)))
        # print(tmp)
        if flag:
            if int('-'+tmp)>-2**31 and int('-'+tmp)<2**31-1:
                return int('-'+tmp)
            else: return 0
        if int(tmp) > -2 ** 31 and int(tmp) < 2 ** 31 - 1:
            return int(tmp)
        else: return 0


def main():
    x = 1534236469
    myResult = Solution()
    print(myResult.reverse(x))

if __name__ == '__main__':
    main()