"""
easy bi-tree
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

if __name__ == '__main__':
    root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    p = TreeNode(5)
    q = TreeNode(1)
    print(Solution().lowestCommonAncestor(root,p,q))