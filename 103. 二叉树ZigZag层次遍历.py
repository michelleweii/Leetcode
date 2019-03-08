# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        res = []
        if root:
            queue.append(root)
            while queue:
                cur_level,cnt_level,size = [],1,len(queue)
                for i in range(size):
                    if cnt_level % 2 != 0:
                        cur = queue.pop()
                        cur_level.append(cur.val)
                        if cur.left:
                            queue.append(cur.left)
                        if cur.right:
                            queue.append(cur.right)
                    else:
                        cur = queue.pop(0)
                        cur_level.append(cur.val)
                        if cur.right:
                            queue.append(cur.right)
                        if cur.left:
                            queue.append(cur.left)

            

                print(cur_level)
                cnt_level+=1

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
    print(Solution().zigzagLevelOrder(a))