"""
middle 2022-01-21 微信、字节
"""
# 关键词：“二叉树 双递归”，类似的题目很多 比如LC 437、LC04.12、LC563

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

