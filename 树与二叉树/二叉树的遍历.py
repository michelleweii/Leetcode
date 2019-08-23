# 迭代
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    stack,res = [],[]
    cur = root
    while stack or cur:# 根节点的右子树还未遍历完，此时cur非空
        while cur:
        # travel to each node's left child, till reach the left leaf
            stack.append(cur)
            cur = cur.left
        if stack: # 可以省略
            # this node has no left child
            cur = stack.pop()
            # so let's append the node value
            res.append(cur.val)
            print(cur.val)
            cur = cur.right
            print(cur)
    return res

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = d
    b.left = c
    b.right = e
    print(inorderTraversal(a))