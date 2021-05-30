"""
middle
dfs
"""
class Solution(object):
    def permute(self, nums):
    """
    非递归
    def permute(self, nums):
        n = len(nums)
        rs = []
        self.perm(nums,0,n,rs)
        print(rs)

    def perm(self, nums, p, q, rs):
        if p == q:
            print(nums)
            rs.append(nums[:])
            # 切片返回新数组，不改变原数组
        for i in range(p, q):
            # for i in range(p, q+1): 这里一直报错
            # 遍历一个数组就是range(0, len(arr))
            # 你第一次调用 传入的q是len(n)，你要遍历数组 就range(0, q)就行，为啥还要+1？
            nums[p], nums[i] = nums[i], nums[p]
            # nums[p]=nums[i]
            self.perm(nums, p+1, q, rs)
            nums[p], nums[i] = nums[i], nums[p]
    """


if __name__ == '__main__':
    nums = [1, 2, 3]
    myResult = Solution()
    myResult.permute([1, 2, 3])
