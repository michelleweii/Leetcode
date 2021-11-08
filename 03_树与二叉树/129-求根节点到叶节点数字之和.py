"""
middle 2021-11-08
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/0-ms-jiao-ke-shu-ji-jie-da-by-liuzhaoce/
标准的回溯模板：（同112、113）https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/biao-zhun-de-hui-su-mo-ban-by-jiubukaiji-t0a2/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:return 0
        return self.helper(root, 0)

    def helper(self, root, i):
        if not root:return 0
        temp = i*10+root.val
        if not root.left and not root.right: # 叶子节点
            return temp
        return self.helper(root.left, temp)+ self.helper(root.right, temp)


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    print(Solution().sumNumbers(a))