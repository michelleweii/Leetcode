"""
middle 2021-11-02
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/
解法1的图解比较容易理解
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        # 左子树为 null，直接考虑下一个节点
        while root: # 注意这里是root不等于空，不是root.left不等于空
            # 如果该节点没有左子树，则移动到右子树上，开始新一轮遍历
            if root.left is None:
                root = root.right
            else:
                # 1、找左子树最右边的节点（案例是4）
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 2、将原来的右子树接到左子树的最右边节点（案例5接到4下面）
                pre.right = root.right
                # 3、将root的左子树插入到右子树的地方（1的right接2）
                root.right = root.left
                root.left = None
                # 4、考虑下一个节点（案例由1移动到2）
                root = root.right
        return
"""
        while (root != None):
            if root.left != None:
                most_right = root.left
                while most_right.right != None: most_right = most_right.right
                most_right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return
"""

if __name__ == '__main__':
    pass
    # root = [1, 2, 5, 3, 4, None, 6]
    # print(Solution().flatten(root))
#     [1,null,2,null,3,null,4,null,5,null,6]
