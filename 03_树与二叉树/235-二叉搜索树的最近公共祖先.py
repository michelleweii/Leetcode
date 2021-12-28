"""
easy 2021-12-29 bst
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉搜索树，右边节点比他大，左边节点比他小
# 递归寻找，若都小于跟结点，递归去左子树找，若都大于根节点，递归去右子树找，一大一小就是根节点
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None


if __name__ == '__main__':
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(8)
    a.left = b
    a.right = c
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)

    # root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    # p = 2
    # q = 8
    print(Solution().lowestCommonAncestor(a, b, c))
