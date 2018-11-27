class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    #