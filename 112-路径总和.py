# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        flag = False
        if root is None:
            return flag
        cur_val = 0
        self.preorder(root,sum,flag,cur_val)


    def preorder(self,node,sum,flag,cur_val):
        if node:
            cur_val += node.val
            # print(cur_val)
            if node.left is None and node.right is None:
                return cur_val == sum

            self.preorder(node.left,sum,flag,cur_val)
            self.preorder(node.right,sum,flag,cur_val)
            cur_val -= node.val


if __name__ == '__main__':
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(5)
    j = TreeNode(1)
    a.right = c
    a.left = b
    b.left = d
    d.left = g
    d.right = h
    c.right = f
    c.left = e
    f.right = j
    f.left = i
    sum = 22
    # Solution().pathSum(a, sum)
    print(Solution().hasPathSum(a,sum))




