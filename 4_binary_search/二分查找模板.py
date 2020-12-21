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