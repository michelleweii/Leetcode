"""
hard 二叉树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

if __name__ == '__main__':
    root = [1,2,3,None,None,4,5]
    codec = Codec()
    codec.deserialize(codec.serialize(root))