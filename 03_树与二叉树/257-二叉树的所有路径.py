"""
easy 2021-11-14
https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html#%E9%80%92%E5%BD%92
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res, self.path = [], []

    def binaryTreePaths(self, root):
        if not root:return self.res
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:return
        self.path.append(str(root.val))  ## 添加当前node
        # 这才到了叶子节点
        if not root.left and not root.right:
            self.res.append('->'.join(self.path[:]))
            return
        if root.left:
            self.dfs((root.left))
            self.path.pop() # 回溯

        if root.right:
            self.dfs((root.right))
            self.path.pop() # 回溯
        return
# ---------------------------- 2021-11-14 --------------------------------------------------------
    def binaryTreePaths_1(self, root):
        res = []
        if not root:  return res # 如果是叶子节点
        def tree_path(root,path,res):
            # 说明是到了根节点，可以输出
            if (root.left == None) and (root.right == None):
                res.append(path+str(root.val))
                return res
            # 遍历左孩子
            if root.left:
                tree_path(root.left, path+str(root.val)+'->', res) # 隐藏了回溯的逻辑
            # 遍历右孩子
            if root.right:
                tree_path(root.right, path+str(root.val)+'->', res)
            return res
        tree_path(root, '', res)
        return res

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    d = TreeNode(1)
    d.left = b
    d.right = c
    print(Solution().binaryTreePaths(a))
    # ['1->2', '1->3']