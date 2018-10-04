# 利用pow(a, b)函数即可。需要开a的r次方则pow(a, 1/r)。
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        else:
            rs = pow(n,1/3)
            print(rs)
            print(str(rs).split("."))

            if type(rs)!= 'int':
                return False
            else:
                return True





def main():
    n= 9
    myResult = Solution()
    print(myResult.isPowerOfThree(n))
    print(type(3))

if __name__ == '__main__':
    main()