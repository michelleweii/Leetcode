import numpy as np
a = "loveleetcode"
print(a[:-1])
print(a[-5::-1]) # octeelevol

nums1 = [1,2,3]
nums2 = []
print(nums1+nums2) # [1, 2, 3]

for i in range(4):
    i = i + 3
    print(i)

n = 1

print(n//3)
nums = [10,3,8,9,4]
nums.sort()
print(nums)

print("-----------")
scales = 2**np.arange(3,6)
print(scales)

import re
a = "Hello world!How are you?My friend.Tom"
print(re.split(" |!|\?|\.", a))

sss = "abc"
print(sss[2:3]) #c
print(sss[2:4]) #c
print(sss[2:5]) #c


a = [5, 2, 3, 1, 4]
print(sorted(a)) # 升序
print(a)
# [1, 2, 3, 4, 5]
# [5, 2, 3, 1, 4] sorted不改变原list
print(sorted(a,reverse=True)) # 实现降序
# [5, 4, 3, 2, 1]


import os
import sys
# 打开文件
path = "/Users/weiwenjing/Documents/2018spring"
dirs = os.listdir(path)
# 是一个列表 ['.DS_Store', 'conference', '卡纳赫拉.jpg', 'project', '人工智能前沿']
print(dirs)
print('--------------------------------------')
# 输出所有文件和文件夹
for file in dirs:
    print(file)
# .DS_Store
# conference
# 卡纳赫拉.jpg
# project
# 人工智能前沿


# 求均值
L = [1,2,3,4,5]
print(np.mean(L))

# del[1:3]删除指定区间
L2 = [1,2,3,4,5]
del L2[1:3]
print(L2) # [1, 4, 5]，删除1，2下标
del L2[0]
print(L2) # [4, 5],删除0下标
# del L2
# print(L2) # NameError: name 'L2' is not defined

a = [0, 2, 2, 3]
a.remove(2)
print(a) # [0, 2, 3],删除指定元素

b = [4, 3, 5]
print(b.pop(1)) # 3
print(b) # [4, 5]

s = "abcdefs"
print(s[0:3])

c = "acbed"
print(sorted(c))

seats = [0,1,1,0,0,0]
print(seats.index(1))


alist = [1,2,3,4]
print(alist[0:3:2]) # [1, 3]
print(alist[1:]) # [2, 3, 4]
print(alist[2:]) # [2, 3, 4]
print(alist[3:]) # [4]
print(alist[4:]) # []

ii = 5
print(ii//2+1)

listNode = [1,2,3]
print(listNode[::-1])

for i in range(4):
    print(i) # 0,1,2,3


A = [1,2,3]
print("origin A:{}".format(A))
A[0] = A[2]
print("changed A:{}".format(A))

colors = ['b','a','c','d']
for i in range(0,len(colors)):
    print(i,colors[i])

a = [0 for _ in range(3)]
# b = [a for _ in range(3)]
# print(b) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [list(a) for _ in range(3)]
print(b) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0):
    print(i) # 啥也不输出


print('')
print('-----------------2019/1/3--------------------------')



rs = ['123','245','345']
for s in rs:
    print(s)
# 123
# 245
# 345

n1 = list(np.full((1,3),2))
n2 = list(np.full((1,3),3))
n3 = list(np.full((1,3),4))
m = n1+n2+n3
# print(m[0,:])
# print(m)

A = [[1,2,3,4,5,6],
[7,8,9,10,11,12],
[13,14,15,16,17,18]]
A = np.mat(A)
print(A[0,:]) # [[1 2 3 4 5 6]]
print(A[0,:1]) #[[1]]
print(A[0,:4]) # [[1 2 3 4]]
print(A[0,:5]) # [[1 2 3 4 5]]


"""
# 用列表生成m行n列的矩阵
m,n = map(int,input().split())
matrix = [[0]*(m)]*(n)
print(matrix)
# 2 3
# [[0, 0], [0, 0], [0, 0]]
# 这种方式生成的矩阵存在一定的问题，比如，无法给特定位置的元素赋值，例如：
matrix[1][1] = 9
print(matrix)
# [[0, 9], [0, 9], [0, 9]]
# 可见，第二列的元素全部被赋值为9了

# 采用numpy生成想要维度的矩阵
x,y = map(int,input().split())
a = np.ones((x+1,y+1))
print(a)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
a[1][1] = 9
print(a)
# [[1. 1. 1. 1. 1.]
#  [1. 9. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
"""

# x,y = map(int,input().split())
x,y = 2,4
A = np.ones((x+1,y+1))
for i in range(0,x+1):
    A[i][0] = i
    for j in range(1,y+1):
        A[i][j] = A[i][j-1]+1
print(A)
# [[ 1.  1.  1.  1.  1.]
#  [ 1.  2.  3.  4.  5.]
#  [ 1.  3.  6. 10. 15.]]

abc = [1,2,3,4]
del abc[-1]
print(abc) # [1, 2, 3]
print(abc[-2])
