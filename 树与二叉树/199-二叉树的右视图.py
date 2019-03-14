# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        queue = []
        if root:
            queue.append(root)
            while queue:
                cur_level,size = [],len(queue)
                for _ in range(size):
                    tmp = queue.pop(0)
                    cur_level.append(tmp.val)
                    if tmp.left:
                        queue.append(tmp.left)
                    if tmp.right:
                        queue.append(tmp.right)
                res.append(cur_level[-1])
        return res



if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    print(Solution().rightSideView(a))