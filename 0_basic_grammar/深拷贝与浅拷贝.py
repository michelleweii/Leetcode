# -*- coding:utf-8 -*-
nums = "abc"
print(id(nums)) # 4540322232
a = nums[1:2] # 4525767688
print(a) # b
print(id(a)) # 4540204792 # 切片重新分配了地址
print(nums) # abc
print(id(nums)) # 4540322232


b = nums[:]
print(b) # abc
print(id(b)) # 4540322232 # 和nums的地址相同，因为string是基本数据类型！！！
print(nums) # abc
print(id(nums)) # 4540322232

nums = "123abc"
print(b) # abc
print(id(b)) # 不随着nums新改变而改变 4540322232
print(nums) # 123abc
print(id(nums)) # 分配了新的地址，与b（=之前的nums）的地址不同, 4541753304

# 堆内存栈内存、深浅拷贝，是针对复杂数据类型—-—对象、列表、字典这种

rs = []
print(id(rs)) # 4356762632
rs.append(3)
rs.append(4)
print(rs) # [3, 4]
print(id(rs)) # 4356762632
new_rs = rs[:]
print(new_rs) # [3, 4]
print(id(new_rs)) # 4356797640, 这里和上面的string就不同了，这里地址就变化了
rs.append([5,6])
print(new_rs) # [3, 4]
