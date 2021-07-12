# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        elif abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        # 以下没想到
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            # 左子树高度
            LD = self.maxDepth(root.left)
            # 右子树高度
            RD = self.maxDepth(root.right)
            return max(RD, LD) + 1


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