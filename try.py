nums = "abc"
rs = []
print(id(nums)) # 4540322232
print(id(rs)) # 4546206728
a = nums[1:2] # 4525767688
print(a) # b
print(id(a)) # 4540204792 # 切片重新分配了地址
print(nums) # abc
print(id(nums)) # 4540322232


b = nums[:]
print(b) # abc
print(id(b)) # 4540322232 # 和nums的地址相同
print(nums) # abc
print(id(nums)) # 4540322232

nums = "123abc"
print(b) # abc
print(id(b)) # 不随着nums新改变而改变 4540322232
print(nums) # 123abc
print(id(nums)) # 分配了新的地址，与b（=之前的nums）的地址不同, 4541753304
