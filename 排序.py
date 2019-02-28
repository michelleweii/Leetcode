# 快排排序
def QuickSort(nums,l,r):
    i = l
    j = r
    if(i<j): # 大循环，控制整个
        temp = nums[i] # 以第一个元素作为比较标准，比它大的都移到后面，比它小的都移到前面
        while(i!=j): # 小循环，控制当前处理的一段
            while(j>i and nums[j]>temp): j-=1
            if(i<j): # 从右向左，找到了比temp小的元素
                nums[i]=nums[j]
                i+=1 # 别忘了！！

            while(i<j and nums[i]<temp): i+=1
            if(i<j):
                nums[j]=nums[i]
                j-=1
        nums[i]=temp

        QuickSort(nums,l,i-1)
        QuickSort(nums,i+1,r)
    return nums

# 冒泡排序
def BubbleSort(nums):
    n = len(nums)-1 # 从最后一个元素开始，然后n-1,n-2,因为此时已经有了最大的冒到最后。
    for i in range(n,-1,-1): # 控制未排序的长短，已经冒上来的（位于最后）不再做处理
        flag = 0
        for j in range(1,i+1,1): # 对未排序的部分，进行两两交换比较
            if(nums[j-1]>nums[j]):
                nums[j-1],nums[j] = nums[j],nums[j-1]
                flag = 1

        if(flag==0): # 没有数据进行交换
            return nums

# 简单选择排序
def SelectSort(nums):
    n = len(nums)
    for i in range(0,n,1):
        k = i
        # 从无序序列中挑出一个最小的元素
        for j in range(i+1,n,1):
            if nums[k]>nums[j]:
                k = j
        # 最小元素与无序序列第一个元素交换
        nums[k],nums[i]=nums[i],nums[k]
    return nums


# 堆排序
def Sift(nums,low,high):
    i = low
    j = 2*i+1
    # temp存储父节点
    # temp = nums[i]
    # 与孩子节点做比较，建堆
    while(j<=high):
        # 找到最大的那个孩子
        if(j<high and nums[j]<nums[j+1]):
            j+=1
        # 父亲和孩子交换
        if nums[i]<nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
            # 继续向下调整
            i = j
            j = 2*i+1
        else:
            break
    # nums[i]=temp

def heapSort(nums):
    n = len(nums)-1 # 这里不减1是因为nums是完全二叉树，元素的存储必须从1开始。
    # 从第一个非叶子节点开始构建初始堆
    for i in range(n//2,-1,-1):
        Sift(nums,i,n)

    # 进行n-1次循环完成堆排序
    for i in range(n,0,-1):
        # 换出根节点，将其放在最终位置（根节点和最后一个元素交换）
        nums[0],nums[i]=nums[i],nums[0]
        # 在减少了1个元素的无序序列中进行调整（剩余部分调整堆）
        Sift(nums,0,i-1)
    return nums


def MergeSort():
    pass

if __name__ == '__main__':
    nums = [49,38,65,200,97,76,13,27,49,100]
    print(QuickSort(nums,0,len(nums)-1))
    print(BubbleSort(nums))
    print(heapSort(nums))
    print(SelectSort(nums))
    print(MergeSort(nums))