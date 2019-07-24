# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        self.res = 0
        self.merge(data)
        return self.res

    def merge(self, data):
        # 归并排序,case ac:50%
        n = len(data)
        if n<=1:return data
        mid = n//2
        left_li = self.merge(data[:mid])
        right_li = self.merge(data[mid:])
        l_p,r_p=0,0
        temp = []
        while l_p<len(left_li) and r_p<len(right_li):
            if left_li[l_p]<=right_li[r_p]:
                temp.append(left_li[l_p])
                l_p+=1
            else:
                # 当左边大于右边时
                temp.append(right_li[r_p])
                # print(len(left_li))
                self.res += (len(left_li)-l_p)
                r_p+=1
        temp += left_li[l_p:]
        temp += right_li[r_p:]
        return temp

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,0]
    print(Solution().InversePairs(data))

    """
    归并排序
    def merge_sort(self,alist):
    # 归并排序
    n = len(alist)
    if n<=1:return alist
    mid = n//2
    left_li = self.merge(alist[:mid])
    right_li = self.merge(alist[mid:])
    left_pointer,right_pointer=0,0
    res = []
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer]<=right_li[right_pointer]:
            res.append(left_li[left_pointer])
            left_pointer+=1
        else:
            res.append(right_li[right_pointer])
            right_pointer+=1
    res += left_li[left_pointer:]
    res += right_li[right_pointer:]
    return res
    """