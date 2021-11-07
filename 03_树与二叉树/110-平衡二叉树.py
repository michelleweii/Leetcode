"""
easy 2021-11-06
平衡二叉树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        if not root:return True
        elif abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        # 以下没想到，需要左子树和右子树同时满足是平衡二叉树的条件
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root: return 0
        else:
            # 左子树高度
            LD = self.maxDepth(root.left)
            # 右子树高度
            RD = self.maxDepth(root.right)
            return max(RD, LD) + 1 # +1是根节点也要计算

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    print(Solution().isBalanced(a))