# -*- coding:utf-8 -*-
# 完全不记得怎么做
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here

if __name__ == '__main__':
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    # d = TreeNode(3)
    # e = TreeNode(6)
    a.right = c
    a.left = b
    print(Solution().KthNode(a))