# 快排
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



if __name__ == '__main__':
    nums = [49,38,65,97,76,13,27,49]
    print(QuickSort(nums,0,len(nums)-1))