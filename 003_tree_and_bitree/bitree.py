# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        if not root:  # 如果是叶子节点
            return []
        res = []
        def tree_path(root, path, res):
            if root.left==None and root.right==None:
                # 如果是叶子节点
                res.append(path+str(root.val))
                return res
            if root.left:
                tree_path(root.left, path+str(root.val)+'->', res)
            if root.right:
                tree_path(root.right, path+str(root.val)+'->', res)
            return res
        tree_path(root, '', res)
        return res


def main():
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    rs = Solution()
    print(rs.binaryTreePaths(node1))



if __name__ == '__main__':
    main()

