# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1.使用何种数据结构存储遍历路径上的节点？
# 2.在树的前序遍历时做什么？后序遍历时做什么？
# 3.如何判断一个节点为叶节点？当遍历到叶节点时应该做什么？
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        rs = []
        path = []
        path_value = 0
        if root is None:
            return rs
        # return self.preorder(root,sum,path,path_value,rs) # 是None
        self.preorder(root, sum, path, path_value, rs)
        # 因为Python是引用传值，所以这个时候执行完preorder函数，rs已经改变了
        return rs



    def preorder(self,node,sum,path,path_value,rs):
        # 深度遍历——前序遍历
        if node is None:
            return

        # 此时访问node为前序遍历
        # 遍历一个节点即更新一次路径值
        path.append(node.val)
        path_value += node.val
        # print(path)

        # 此时访问node为中序遍历
        if node.right is None and node.left is None and path_value == sum:
            # print(path)
            # rs.append(path.copy())  # path.copy()leetcode ide无法通过
            rs.append(path[:])
            # print(rs)

        self.preorder(node.left, sum, path, path_value, rs)
        self.preorder(node.right, sum, path, path_value, rs)
        # 此时访问node为后序遍历
        # 遍历完成后，叶子节点出栈

        # 这一块的顺序不知道到底放在哪里？
        # 答：左右子树全部访问完，说明以它为根节点的这颗子树已经访问完了，
        # 以它为根节点的所有可能性都尝试了，然后就换一个结点为根节点呀
        del path[-1]
        path_value -= node.val

if __name__ == '__main__':
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(5)
    j = TreeNode(1)
    a.right = c
    a.left = b
    b.left = d
    d.left = g
    d.right = h
    c.right = f
    c.left = e
    f.right = j
    f.left = i
    sum = 22
    # Solution().pathSum(a, sum)
    print(Solution().pathSum(a,sum))

