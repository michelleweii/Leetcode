'''
# 349
# 给定两个数组，编写一个函数来计算它们的交集。
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rs = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        # print(nums1)
        # print(nums2)
        for i in nums1:
            for j in nums2:
                if i==j:
                    rs.append(i)
                    break
        rs = list(set(rs))
        return rs
# 别人的
#
# a = set(nums1)
# b = set(nums2)
# res =[]
# for i in a:
#   if i in b:
        res.append(i)
# return res
#



def main():
    a = [4,9,5]
    b = [9,4,9,8,4]
    myresult = Solution()
    print(myresult.intersection(a,b))

if __name__ == "__main__":
    main()
'''

# 350
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rs = []
        flag = []
        for i,val_i in enumerate(nums1):
            for j,val_j in enumerate(nums2):
                if (val_i==val_j) and (j not in flag):
                    flag.append(j)
                    rs.append(val_i)
                    break
        return rs



def main():
    a = [1,2,2,1]
    b = [2,2]
    myresult = Solution()
    print(myresult.intersect(a,b))

if __name__ == "__main__":
    main()