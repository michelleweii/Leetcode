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
    n = len(nums)-1
    for i in range(n,-1,-1): # 控制未排序的长短，已经冒上来的（位于最后）不再做处理
        flag = 0
        for j in range(1,i+1,1): # 对未排序的部分，进行两两交换比较
            if(nums[j-1]>nums[j]):
                nums[j-1],nums[j] = nums[j],nums[j-1]
                flag = 1

        if(flag==0): # 没有数据进行交换
            return nums

# 简单选择排序
def


if __name__ == '__main__':
    nums = [49,38,65,97,76,13,27,49,100]
    print(QuickSort(nums,0,len(nums)-1))
    print(BubbleSort(nums))