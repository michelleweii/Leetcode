"""
easy 2021-12-02
"""
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None: return 0
        # 左子树高度
        LD = self.maxDepth(root.left)
        # 右子树高度
        RD = self.maxDepth(root.right)
        return max(RD,LD)+1

    # 定义queue，层次队列
    def maxDepth2(self, root):
        if not root:return 0
        tqueue, h = collections.deque(), 0
        tqueue.append(root)
        while tqueue:
            nextlevel = collections.deque()
            while tqueue:
                front = tqueue.popleft()
                if front.left:
                    nextlevel.append(front.left)
                if front.right:
                    nextlevel.append(front.right)
            tqueue = nextlevel
            h += 1
        return h

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
    print(Solution().maxDepth(a))