"""
middle 2021-12-23 链表/栈
对比lc2
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

if __name__ == '__main__':
    # l1 = [7, 2, 4, 3], l2 = [5, 6, 4]
    # [7,8,0,7]
    l1 = ListNode(7)
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    l1.next, a.next, b.next = a, b, c
    l2 = ListNode(5)
    d = ListNode(6)
    e = ListNode(4)
    l2.next, d.next = d, e
    print(Solution().addTwoNumbers(l1,l2))