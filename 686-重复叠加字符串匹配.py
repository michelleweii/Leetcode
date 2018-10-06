class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if set(A)!=set(B):
            return -1
        tmp = A
        i = 2
        while i<10000:
            if B in A:
                return i-1
            else:
                A=tmp*i
                i+=1

        return -1
def main():
    A = "abcds"
    B = "cdabcdab"
    myresult = Solution()
    print(myresult.repeatedStringMatch(A, B))

if __name__ == "__main__":
    main()