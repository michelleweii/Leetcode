# 给定一个排序数组，你需要在原地删除重复出现的元素，
# 使得每个元素最多出现两次，返回移除后数组的新长度。

# 27,26，283思路相同
class Solution:
    def removeDuplicates(self, nums):
        i = 0 
        flag = 0
        while i<len(nums)-2:
            # flag = 0
            if nums[i]==nums[i+2]:
                flag = 1
                del nums[i+2]
                # print(nums)
            if not flag:
                i = i+2
            else:
                flag = 0
            # print(i)
        return len(nums)
            
    def test(self,nums):
        print(nums.count(1)) # 3

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    # nums = [0,0,1,1,1,1,2,3,3]
    # nums = [1,1,1,1]
    res = Solution()
    print(res.removeDuplicates(nums))
    # Solution().test(nums)