# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    print(Solution().deleteDuplicates(a))
