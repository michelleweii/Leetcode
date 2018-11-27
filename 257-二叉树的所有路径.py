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

if __name__ == '__main__':
