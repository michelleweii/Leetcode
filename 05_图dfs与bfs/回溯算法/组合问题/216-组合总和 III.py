# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。
class Solution:
    def combinationSum3(self, k, n):
        path=[]
        result=[]
        nums = [i for i in range(1,10)]
        self.dfs(nums,k,n,0,path,result)
        return result

    def dfs(self,nums,k,n,start,path,result):
        if len(path)==k and n==0 and path not in result:
            result.append(path[:])
            return
        for i in range(start,len(nums)):
            if nums[i]>n or k<0:
                return
            # k-=1
            path.append(nums[i])
            self.dfs(nums,k,n-nums[i],i+1,path,result)
            # k+=1
            path.pop()



if __name__ == '__main__':
    k = 3
    n = 9
    print(Solution().combinationSum3(k,n))