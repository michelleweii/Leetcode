from collections import deque
# 小结：
# 层次遍历是广度优先遍历
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 2020/02/23
    def zigzagLevelOrder(self, root):
        if root is None: return []
        queue = deque([root])
        path = []
        flag = 1
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            path.append(cur_level[::flag])
            flag *= -1
        return path

    def zigzagLevelOrder2(self, root):
        queue = []
        res = []
        if root:
            queue.append(root)
            flag = 1
            while queue:
                cur_level, size = [], len(queue)
                for i in range(size):
                    cur = queue.pop(0)
                    cur_level.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                res.append(cur_level[::flag])
                flag *= -1
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
    print(Solution().zigzagLevelOrder(a))