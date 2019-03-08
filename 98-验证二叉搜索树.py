# Definition for a binary tree node.
# 方法一：中序遍历二叉树，结果是否是递增的，递增代表是二叉搜索树。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        res = []
        self.helper(root,res)
        # print(res)
        for i in range(1,len(res)):
            if res[i-1]>=res[i]:
                return False
        return True

    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            # print(res)
            self.helper(root.right,res)
        return None


    # def isValidBST1(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root is None:
    #         return False
    #     if root.left.val <= root.val:
    #         return self.isValidBST(root.left)
    #     else:
    #         return self.isValidBST(root.right)




if __name__ == '__main__':
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    # d = TreeNode(3)
    # e = TreeNode(6)
    a.right = c
    a.left = b
    # c.right = e
    # c.left = d

    print(Solution().isValidBST(a))