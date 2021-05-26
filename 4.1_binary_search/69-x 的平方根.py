class Solution:
    def mySqrt(self, x):
        left = 1
        right = x//2
        if(x == 0):
            return 0
        def search(l, r):
            if(int(l) >= int(r)):
                return int(l)
            mid = (l+r) / 2
            if(mid*mid>x):
                return search(l, mid)
            elif(mid*mid<x):
                return search(mid, right)
            else:
                return int(mid)
        return search(left, right)
        # if x<=0:
        #     return -1
        # else:
        #     low = 0
        #     high = x
        #     mid = (low+high)//2
        #     while abs(mid*mid-x)!=0:
        #         if mid*mid>x:
        #             high = mid
        #         else:
        #             low = mid
        #         mid = (low+high)/2
        # return mid

        # gg2
        # if x == 0:
        #     return 0
        # i = 1; j = x / 2 + 1
        # while( i <= j ):
        #     center = ( i + j ) / 2
        #     if center ** 2 == x:
        #         return center
        #     elif center ** 2 > x:
        #         j = center - 1
        #     else:
        #         i = center + 1
        # return int(j)



if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))