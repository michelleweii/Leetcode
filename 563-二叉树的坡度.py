# https://blog.csdn.net/weixin_40449300/article/details/81051179
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

    def add(self,item):
        # 最后去添加，不考虑头插还是尾插
        node = TreeNode(item)
        if self.val is None:
            self.val = node
            return
        queue = [self.val]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                # 左节点为空，新加入的节点放到这个位置上
                cur_node.left=node
                return
            else:
                # 不是空的话，左节点入队
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right=node
                return
            else:
                queue.append(cur_node.right)

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum_and_tilt(root):
            if not root:        # 如果是一个叶子节点的左右孩子，则是空的，没有东西可以继续遍历了！
                return 0,0  # 第一个值是该节点为根的时候，它的和；第二个值是该节点的
                            # 总坡度（因为题目要求的是所有节点的坡度之和）
            sum_left,left_tilt = sum_and_tilt(root.left)
            sum_right,right_tilt = sum_and_tilt(root.right)
            return sum_left+sum_right+root.val,abs(sum_left-sum_right)+left_tilt+right_tilt

        sum_tree,tilt_tree = sum_and_tilt(root)
        return  tilt_tree


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    ans = Solution()
    print(ans.findTilt(tree))
