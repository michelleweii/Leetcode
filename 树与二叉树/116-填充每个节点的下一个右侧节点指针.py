# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        # 不需要判断root.right是否为null
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:root.right.next = None
            self.connect(root.left)
            self.connect(root.right)
        return root


