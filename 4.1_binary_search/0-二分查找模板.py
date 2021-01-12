def check(value):
    pass

# <= 目标值的最大位置
def bsearch_1(l, r):
    while (l < r):
        mid = (l+r) // 2
        # 求最大值
        if check(mid): r = mid
        else: l = mid+1
    return l

# >= 目标值的最小位置
def bsearch_2(l, r):
    while(l<r):
        mid = (l+r+1) // 2
        # 求最小值
        if check(mid): l = mid
        else: r = mid-1
    return l


if __name__ == '__main__':
    sum = (4+2)>>1
    print(sum) # 3


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