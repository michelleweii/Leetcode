# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res1,res2 = [],[]
        if self.preorder(p,res1)==self.preorder(q,res2):
            return True
        return False

    def preorder(self,root,res):
        if root:
            res.append(root.val)
            if root.left:
                self.preorder(root.left,res)
            else:
                res.append('null')
            if root.right:
                self.preorder(root.right,res)
            else:
                res.append('null')
        return res
    #
    # def postorder(self,root,res):
    #     if root:
    #         if root.left:
    #             self.preorder(root.left,res)
    #         if root.right:
    #             self.preorder(root.right,res)
    #         res.append(root.val)
    #     return res



if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)

    c = TreeNode(1)
    d = TreeNode(2)

    a.left = b
    c.right = d
    print(Solution().isSameTree(a,c))