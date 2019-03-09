# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root,res)
        return res

    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)

    # 迭代
    def inorderTraversal(self, root):
        stack,res = [],[]
        cur = root
        while stack or cur:
            while cur:
            # travel to each node's left child, till reach the left leaf
                stack.append(cur)
                cur = cur.left
            if stack: # 可以省略
                # this node has no left child
                cur = stack.pop()
                # so let's append the node value
                res.append(cur.val)
                cur = cur.right
        return res



if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    print(Solution().inorderTraversal(a))