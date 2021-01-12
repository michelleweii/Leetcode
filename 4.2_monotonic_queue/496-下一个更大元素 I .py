# -*- coding:utf-8 -*-
class Solution(object):
    """
    2021/01/12 单调队列
    """


    def nextGreaterElement(self, findNums, nums):
        rs = []
        for i, val_i in enumerate(findNums):
            flag = 0
            for j, val_j in enumerate(nums):
                if (val_j == val_i):
                    flag = 1
                if (flag and val_j > val_i):
                    rs.append(val_j)
                    break
                if (j == len(nums) - 1):
                    rs.append(-1)
        return rs

if __name__ == "__main__":
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    myresult = Solution()
    print(myresult.nextGreaterElement(nums1, nums2))
