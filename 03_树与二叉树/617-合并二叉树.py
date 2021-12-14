"""
easy 2021-12-14
https://leetcode-cn.com/problems/merge-two-binary-trees/solution/dong-hua-yan-shi-di-gui-die-dai-617he-bing-er-cha-/
同时遍历2个树，每次将新的值更新在root1上，最后返回root1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 总结下递归的条件：
#
# 终止条件：树 1 的节点为 null，或者树 2 的节点为 null
# 递归函数内：将两个树的节点相加后，再赋给树 1 的节点。再递归的执行两个树的左节点，递归执行两个树的右节点
#
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode): #-> TreeNode:
        if root1 is None: return root2
        if root2 is None: return root1

        return self.preorder(root1, root2)

    def preorder(self, r1, r2):
        # 前序遍历，每次将节点值求和，更新到root1上
        # 出口
        if not r1:return r2
        if not r2:return r1

        r1.val += r2.val
        r1.left = self.preorder(r1.left, r2.left)
        r1.right = self.preorder(r1.right, r2.right)
        return r1

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)
    a.right = b
    a.left = c
    c.left = d

    a1 = TreeNode(2)
    b1 = TreeNode(1)
    c1 = TreeNode(3)
    d1 = TreeNode(4)
    e1 = TreeNode(7)

    a1.right = c1
    a1.left = b1
    b1.right = d1
    c1.right = e1
    print(Solution().mergeTrees(a,a1))