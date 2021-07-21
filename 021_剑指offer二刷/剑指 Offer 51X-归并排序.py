
# 归并排序
def merge_sort1():
    pass

def merge_sort2(nums, l, r):
    if l >= r: return
    mid = (l + r) // 2
    mergesort(nums, l, mid - 1)
    mergesort(nums, mid, r)

    left_p, right_p = l, mid
    temp = []
    while left_p <= mid - 1 and right_p <= r:
        if nums[left_p] <= nums[right_p]:
            temp.append(nums[left_p])
            left_p += 1
        else:
            temp.append(nums[right_p])
            right_p += 1

    temp += nums[left_p:mid]
    temp += nums[right_p:r + 1]

    for k in range(r - l + 1):
        nums[l + k] = temp[k]
    return nums


def mergesort(nums,l,r):
    if l>=r: return
    mid = (l+r)//2
    mergesort(nums,l,mid)
    mergesort(nums,mid+1,r)
    i,j=l,mid+1
    temp = []
    while i<=mid and j<=r:
        if nums[i]<nums[j]:
            temp.append(nums[i])
            i+=1
        else:
            temp.append(nums[j])
            j+=1
    if i<=mid:temp.extend(nums[i:mid+1])
    if j<=r  :temp.extend(nums[j:r+1])
    for i in range(r-l+1):
        nums[l+i] = temp[i]
    return nums


if __name__ == '__main__':
    nums = [3,2,1]
    b = mergesort(nums, 0, len(nums)-1)
    print("b", b)
    # a = merge_sort(nums, 0, len(nums)-1)
    # print(nums)
    # print("a", a)

    c = merge_sort2(nums, 0, len(nums)-1)
    print("c", c)

