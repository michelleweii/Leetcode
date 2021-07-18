"""
middle
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':


if __name__ == '__main__':
    n = 10
    print(Solution().treeToDoublyList(n))