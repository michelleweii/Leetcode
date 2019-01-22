# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """




if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(7)
    f = TreeNode(4)
    g = TreeNode(1)
    h = TreeNode(0)
    i = TreeNode(8)
    # j = TreeNode(1)
    a.right = g
    a.left = b
    b.left = c
    b.right = d
    d.left = e
    d.right = f
    c.right = f
    c.left = e
    g.right = i
    g.left = h
    p = 5
    q = 1
    print(Solution().lowestCommonAncestor(a,p,q))