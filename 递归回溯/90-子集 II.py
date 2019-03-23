# 给定一个可能包含重复元素的整数数组 nums，
# 返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort() # 这句话好神奇，加了就对了 （说明：解集不能包含重复的子集。）
        self.dfs(0, [], nums, res)
        return res

    def dfs(self, i, item, nums, res):
        if i >= len(nums):
            return
        item.append(nums[i]) # 每个阶段的元素
        res.append(item[:])
        self.dfs(i+1,item,nums,res)
        item.pop()
        self.dfs(i+1,item,nums,res)


if __name__ == '__main__':
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))


# 输入：
# [4,4,4,1,4]
# 输出：
# [[],[4],[4,4],[4,4,4],[4,4,4,1],[4,4,4,1,4],[4,4,4,4],[4,4,1],[4,4,1,4],[4,1],[4,1,4],[1],[1,4]]
# 预期：
# [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]