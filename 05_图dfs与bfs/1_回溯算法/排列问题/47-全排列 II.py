class Solution:
    def permuteUnique(self, nums):
        result = []
        self.dfs(nums,0,[],result)
        print(list(result))

    def dfs(self,nums,start,path,result):
        if len(path)==len(nums):
            if path not in result:
                result.append(path[:])
            return
        for i in range(start,len(nums)):
            path.append(nums[i])
            self.dfs(nums,i+1,path,result)
            # path.pop()


if __name__ == '__main__':
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))
