# 《剑指offer》面试题3
# using hash
def find(nums):
    n = len(nums)
    nums_dict={}
    for i in range(n):
        if nums[i] not in nums_dict:
            nums_dict[nums[i]] = i
        else:
            return nums[i]
    return -1

if __name__ == '__main__':
    nums = [2,3,1,0,2,5,3]
    print(find(nums))