# -*- coding:utf-8 -*-
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
        res = []
        if not root:  # 如果是叶子节点
            return []
        res = []
        def tree_path(root,path,res):
            if root.left==None and root.right==None:
                res.append(path+str(root.val))
                return res
            if root.left:
                tree_path(root.left,path+str(root.val)+'->',res)
            if root.right:
                tree_path(root.right,path+str(root.val)+'->',res)
            return res
        tree_path(root,'',res)
        return res


def main():
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree1 = TreeNode(1)
    tree1.left = tree2
    tree1.right = tree3
    rs = Solution()
    print(rs.binaryTreePaths(tree1))



if __name__ == '__main__':
    main()

