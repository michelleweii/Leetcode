# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root, root)
    # 还可以考虑使用层次遍历，判断是否是回文数


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = g
    c.left = f

    print(Solution().isSymmetric(a))
