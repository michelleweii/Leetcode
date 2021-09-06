"""
easy 2021-09-06
双指针
https://leetcode-cn.com/problems/remove-element/solution/shua-chuan-lc-shuang-bai-shuang-zhi-zhen-mzt8/
"""
class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        if not n:return nums
        i,j = 0,n-1
        while i<j:
            while nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
            else:
                i+=1
        print(nums[:i+1])

if __name__ == '__main__':
    # nums = [0,1,2,2,3,0,4,2]
    # val = 2
    nums = [3, 2, 2, 3]
    val = 3
    myResult = Solution()
    print(myResult.removeElement(nums,val))

