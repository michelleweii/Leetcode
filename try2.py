a = 1
b = 1
print(a is b) # True

import collections
n1 = '2500'
n2 = '0052'

print(collections.Counter(n1)==collections.Counter(n2))

str1 = "w20930"
print(str1.split('0'))


alist = [1,2,3,4,5]
for _ in range(len(alist)):
    print(alist.pop())



"""
二分查找
def BiSearch(nums,k):
    nums = sorted(nums)
    print(nums)
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==k:
            return True
        if nums[mid]<k:
            low = mid+1
        else:
            high = mid-1
    return -1
if __name__ == '__main__':
    nums = [3,5,74,2,75,8,2,9]
    k = 9
    print(BiSearch(nums, k))
"""

# 浅拷贝
list1 = [[]]*3
print(list1) # [[], [], []]
list1[0].append(3) # [[3], [3], [3]]
# 是一个含有一个空列表元素的列表,所以[[]]*3表示3个指向这个空列表元素的引用,修改任何
# 一个元素都会改变整个列表
print(list1)

# 深拷贝
lists = [[] for i in range(3)]
lists[0].append(3)
lists[0].append(4)
lists[0].append(5)
print(lists) # [[3, 4, 5], [], []]

# 构建3行4列二维数组
myList = [([0] * 3) for i in range(4)]
print(myList) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

