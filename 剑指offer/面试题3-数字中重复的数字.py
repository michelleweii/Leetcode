# 《剑指offer》面试题3
# using hash
def FindHash(nums):
    n = len(nums)
    nums_dict={}
    for i in range(n):
        if nums[i] not in nums_dict:
            nums_dict[nums[i]] = i
        else:
            return nums[i]
    return -1

def FindExchange(nums):
    pass

# 题目二：不修改数组找出重复的数字
def Find2(nums):
    pass


if __name__ == '__main__':
    nums = [2,3,1,0,2,5,3]
    print("第一题:")
    print(FindHash(nums))
    print(FindExchange(nums))
    print("第二题:")
    print(Find2(nums))