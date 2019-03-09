# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        rs = []
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
                rs.append(cur_level[:])
        return rs

    # 深度优先遍历
    def dfs(self,root):
        stack = []
        rs = []
        if root:
            stack.append(root)
            while stack:
                cur = stack.pop()
                # print(cur.val)
                rs.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        print(rs)


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
    print(Solution().levelOrder(a))
    print(Solution().dfs(a))

