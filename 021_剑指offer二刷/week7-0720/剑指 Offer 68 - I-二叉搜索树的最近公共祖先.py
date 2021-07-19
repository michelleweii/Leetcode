"""
easy bst

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

if __name__ == '__main__':
    root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
    p = TreeNode(2)
    q = TreeNode(8)
    print(Solution().lowestCommonAncestor(root, p, q))
