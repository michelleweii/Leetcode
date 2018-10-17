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