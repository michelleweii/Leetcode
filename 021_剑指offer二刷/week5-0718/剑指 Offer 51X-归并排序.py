
# 归并排序

def merge_sort(nums, l, r):
    # 只剩余一个元素
    if l>=r:return
    # n = len(nums)
    # if n<=1:
    #     return nums
    mid = (l+r)//2
    # mid = n//2
    leftlist = merge_sort(nums[:mid], l, mid-1)
    rightlist = merge_sort(nums[mid:], mid, r)

    res = []
    left_pointer, right_pointer = l, mid
    # while left_pointer<len(leftlist) and right_pointer<len(rightlist):
    while left_pointer <= l and right_pointer <= r:
        if leftlist[left_pointer]<=rightlist[right_pointer]:
            res.append(leftlist[left_pointer])
            left_pointer+=1
        else:
            res.append(rightlist[right_pointer])
            right_pointer+=1
    res += leftlist[left_pointer:]
    res += rightlist[right_pointer:]
    for i in range(r-l+1):
        nums[l+i] = res[i]
    # return res

if __name__ == '__main__':
    nums = [3,2,1]
    a = merge_sort(nums, 0, len(nums)-1)
    print(nums)
    print(a)
    # print(int(str(10)))
    # print(int("hello"))
