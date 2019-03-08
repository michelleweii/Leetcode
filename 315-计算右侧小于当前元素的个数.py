# 思路是归并排序——思路忘记了
# 用二叉搜索树完成

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 0

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pass


if __name__ == '__main__':
    nums = [5,2,6,1]
    print(Solution().countSmaller(nums))