# -*- coding:utf-8 -*-
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        count_A,count_L=0,0
        for i in range(n):
            if s[i]=='A':
                count_A += 1
                if count_A>1:
                    return False
            if s[i]=='L':
                count_L += 1
                if count_L>2:
                    return False
            if s[i] != 'L':
                count_L=0
        return True




def main():
    s = "LLPPPLL"
    myresult = Solution()
    print(myresult.checkRecord(s))



if __name__ == "__main__":
    main()
