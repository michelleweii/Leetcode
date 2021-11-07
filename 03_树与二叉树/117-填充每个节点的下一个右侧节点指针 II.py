


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root is None: return root
        first = root
        while first: # 如果树不为null
            head = tail = Node(0)
            cur = first
            while cur:  # 遍历当前层
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            first = head.next
        return root

if __name__ == '__main__':
    a = Node(1)

