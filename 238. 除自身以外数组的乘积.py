class Solution:
    def productExceptSelf(self, nums):
        if not nums:return []
        n = len(nums)
        B = [0]*n
        p = 1
        for i in range(n):
            B[i]=p
            p*=nums[i]
        for i in range(n-1,0,-1):
            B[i]*=p
            p*=nums[i]
        return B



if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))