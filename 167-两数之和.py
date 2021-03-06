# 有一个样例没有通过16/17,超出时间限制，说明不让暴力求解。

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        暴力
        for i in range(len(numbers)):
            rs = []
            left = target-numbers[i]
            # print(left)
            # rs.append(i+1)
            for j in range(i+1,len(numbers)):
                # print("j")
                # print(j)
                if numbers[j] == left:
                    # print("true")
                    # rs.append(j+1)
                    return [i+1,j+1]
        # print(rs)
        return None
        """
        # 有序数据，利用快排
# 我们可以这样想，我们首先判断首尾两项的和是不是target，如果比target小，
# 那么我们左边+1位置的数（比左边位置的数大）再和右相相加，继续判断。如果比target大，
# 那么我们右边-1位置的数（比右边位置的数小）再和左相相加，继续判断。我们通过这样不断放缩的过程，
# 就可以在O(n)的时间复杂度内找到对应的坐标位置。（这和快速排序的思路很相似）
#
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    myResult = Solution()
    print(myResult.twoSum(numbers, target))

if __name__ == '__main__':
    main()