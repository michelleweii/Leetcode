"""
middle
官方：双指针(严格来说不算双指针)
1、在尽可能靠右的低位进行交换，需要从后向前查找
2、将一个 尽可能小的「大数」 与前面的「小数」交换。
比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
3、将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。
以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；
然后需要将 5 之后的数重置为升序，得到 123546。
显然 123546 比 123564 更小，123546 就是 123465 的下一个排列。

链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
"""
class Solution:
    def nextPermutation(self, nums):
        if len(nums)<1:return nums
        # i是小数、k是大数
        i,j,k = len(nums)-2, len(nums)-1, len(nums)-1
        # 找到i,j // find: A[i]<A[j]
        while i>=0 and nums[i]>=nums[j]:
            i-=1
            j-=1
        # 寻找k，大数
        if i>=0: # 不是最后一个排列
            # // find: A[i] < A[k]
            while nums[i]>=nums[k]:
                k-=1 # j后的数必然降序，现在需要找到比nums[i]大的数
            # // swap A[i], A[k]
            nums[i],nums[k] = nums[k],nums[i]

        # // reverse A[j:end]
        # 将j后面的数字升序
        # 切片操作不是原地操作，所以nums[i+1:].sort()并不是对原数组排序
        # print(i,j)
        nums[j:] = sorted(nums[j:])
        # return nums

"""
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                for j in range(n-1,i,-1):
                    if nums[j] > nums[i]:
                        nums[j] , nums[i] = nums[i] , nums[j]
                        break
                nums[i+1:] = sorted(nums[i+1:])
                return
        else:
            nums[::] = nums[::-1]
"""
if __name__ == '__main__':
    # nums = [1, 2, 3] # 132
    nums = [3,2,1]  # [1,2,3]
    print(Solution().nextPermutation(nums))
