# 此题gg
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) >= 2:
            flag = 0  # 递增
            if A[0] > A[1]: flag = 1 # 递减
            print(flag)
            for i in range(len(A)-1):
                print("i:")
                print(i)
                print(A[i+1])
                print(A[i])
                if A[i+1] < A[i] and flag==0:
                    return False
                elif A[i+1] > A[i] and flag==1:
                    return False
                else:
                    return True
        else:
            return True


def main():
    listA = [1,3,2]
    myResult = Solution()
    print(myResult.isMonotonic(listA))

if __name__ == '__main__':
    main()