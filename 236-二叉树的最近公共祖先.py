# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        finish = 0
        path, p_result, q_result = [],[],[]
        self.preorder(root,p,path,p_result,finish)
        path.clear()
        finish = 0
        self.preorder(root,q,path,q_result,finish)
        path_len = 0
        # 求最短的那个路径
        if p_result<q_result:
            path_len = len(p_result)
        else:
            path_len = len(q_result)
        result = TreeNode(0)
        for i in range(path_len):
            if p_result[i] == q_result[i]:
                # 找到了公共祖先
                result = p_result[i]
        return result.val


    def preorder(self,node,search,path,result,finish):
        # 先序遍历（深度优先遍历）
        # node：正在遍历的结点；search：希望遍历到的结点
        if node is None or finish:
            # 当node为空或已找到search结点，finish=1为找到
            return
        # 先序遍历，将结点压入栈
        path.append(node.val)
        print(path)
        if node == search:
            finish = 1
            result = path
        self.preorder(node.left,search,path,result,finish)
        self.preorder(node.right,search,path,result,finish)
        # 结束遍历node时，将node弹出path栈
        path.pop()







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
    # j = TreeNode(1)
    a.right = g
    a.left = b
    b.left = c
    b.right = d
    d.left = e
    d.right = f
    c.right = f
    c.left = e
    g.right = i
    g.left = h
    p = b
    q = g
    print(Solution().lowestCommonAncestor(a,p,q))