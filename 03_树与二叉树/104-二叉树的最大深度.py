"""
easy 2021-12-02 二叉树属性
计算每个子树的高度，再+1
"""
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
        q, depth = [root], 0
        while q:
            cur_level, size = [],len(q)
            for i in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 出当前层
            depth += 1
        return depth

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
    print(Solution().maxDepth2(a))