class Solution(object):
    def subsetsWithDup(self, nums):
        path = []
        result = []
        nums.sort()
        self.dfs(nums,0,path,result)
        return result

    def dfs(self,nums,start,path,result):
        if path not in result:
            result.append(path[:])
        # 需要一个出口
        if start == len(nums): # 之前报错，改了这里
            return
        for i in range(start,len(nums)):
            path.append(nums[i])
            self.dfs(nums,i+1,path,result)
            path.pop()


if __name__ == '__main__':
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))