# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:  # 如果是叶子节点
            return []
        res = []
        def tree_path(root,path,res):
            if (root.left == None) and (root.right == None):
                res.append(path+str(root.val))
                return res
            if root.left:
                tree_path(root.left,path+str(root.val)+'->',res)
            if root.right:
                tree_path(root.right,path+str(root.val)+'->',res)
            return res
        tree_path(root,'',res)
        return res

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    d = TreeNode(1)
    d.left = b
    d.right = c
    print(Solution().binaryTreePaths(a))
    # ['1->2', '1->3']