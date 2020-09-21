nums = [1,2,3,4,5,6,7,8]
i = 1
n = len(nums)
while len(nums):
    if i%2==1:
        del nums[i]
    n-=1
    i+=1

print(nums)