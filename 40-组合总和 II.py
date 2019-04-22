# 给定一个数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# -----------------------------------------------
# 递归的时候将 idx 加 1（需判断是否超出candidates的范围），另外由于题目输入的candidates可能包含相同的元素，
# 所以我们需要对得到的答案进行去重处理。
class Solution:
    def combinationSum2(self, candidates, target):
        path=[]
        result=[]
        candidates.sort()
        self.dfs(candidates,target,0,path,result)
        return result

    # 我的想法是每次找过的元素都标记一下，然后下次找的时候就不可以选这个了
    # i+1表明一个数字只能使用一次
    def dfs(self,candidates,target,start,path,result):
        # 判断出口
        if target == 0 and path not in result:
            result.append(path[:])
            return
        # 开始循环遍历
        for i in range(start,len(candidates)):
            if candidates[i]>target:
                return
            # i+1表明一个数字只能使用一次，这样下次递归的循环就从i+1开始了
            self.dfs(candidates,target-candidates[i],i+1,path+[candidates[i]],result)


# https://blog.csdn.net/weixin_41958153/article/details/80936849
if __name__ == '__main__':
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    candidates = [2,5,2,1,2]
    target = 5
    print(Solution().combinationSum2(candidates, target))