"""
middle 2021-12-15 bst
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k): #int) -> int:


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)

    c.right = d
    c.left = a
    a.right = b
    k = 1
    print(Solution().kthSmallest(c,k))