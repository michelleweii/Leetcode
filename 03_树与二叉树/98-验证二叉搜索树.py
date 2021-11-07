"""
middle 2021-11-06
已知：BST的中序遍历是升序的
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # 方法一：中序遍历二叉树，结果是否是递增的，递增代表是二叉搜索树。
class Solution(object):
    def isValidBST1(self, root):
        if not root:return root
        res = [] # 存中序遍历的结果
        self.helper(root, res)
        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False
        return True

    def helper(self,root,res):
        # 二叉树中序遍历
        if not root:return root
        self.helper(root.left, res)
        res.append(root.val)
        # print(res)
        self.helper(root.right, res)

# 方法二，递归版本，每个结点都满足左小于它，右大于它的性质
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf"))
    def check_bst(self, node, left, right):
        if not node: return True
        if not left < node.val < right:
            return False
        return (self.check_bst(node.left, left, node.val)
                and self.check_bst(node.right, node.val, right))

if __name__ == '__main__':
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    # d = TreeNode(3)
    # e = TreeNode(6)
    a.right = c
    a.left = b
    # c.right = e
    # c.left = d

    print(Solution().isValidBST(a))