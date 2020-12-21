# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None: return None
        # root为p或者root为q，说明找到了p和q其中一个
        if (root is p) or (root is q): return root
        # 递归调用当前节点的左子树
        left = self.lowestCommonAncestor(root.left,p,q)
        # 递归调用当前节点的右子树
        right = self.lowestCommonAncestor(root.right,p,q)
        # 若左子树找到了p，右子树找到了q，说明此时的root就是公共祖先
        if left and right: return root
        # 若左子树是none,右子树不是，说明右子树找到了A或B
        if not left: return right
        # # 若右子树是none,左子树不是，说明左子树找到了A或B
        if not right:return left
        # 如果左边，右边都没找到呢？


    def lowestCommonAncestor_gg(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        p_path, p_result = [], []
        self.dfs(root, p, p_path, p_result)
        q_path, q_result = [], []
        self.dfs(root, q, q_path, q_result)

        # 求最短的那dfs个路径
        # print("p:",p_result)
        # print("q:",q_result)

        if len(p_result)<len(q_result):
            path_len = len(p_result)
        else:
            path_len = len(q_result)

        result = TreeNode(0)
        for i in range(path_len):
            if p_result[i].val == q_result[i].val:
                result = p_result[i]

        return result


    def dfs(self,node,search,path,result):
        # 先序遍历（深度优先遍历）
        # node：正在遍历的结点；search：希望遍历到的结点
        if node:
            # 当node为空或已找到search结点，finish=1为找到
            path.append(node)
            while path:
                node = path.pop()
                result.append(node)
                # print(result)
                if node.val == search.val:
                    return result
                if node.right:
                    path.append(node.right)
                if node.left:
                    path.append(node.left)
        return result

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(7)
    f = TreeNode(4)
    g = TreeNode(1)
    h = TreeNode(0)
    i = TreeNode(8)

    a.right = g
    a.left = b
    b.left = c
    b.right = d
    d.left = e
    d.right = f
    g.right = i
    g.left = h

    p = TreeNode(5)
    q = TreeNode(1)
    print(Solution().lowestCommonAncestor(a,p,q))