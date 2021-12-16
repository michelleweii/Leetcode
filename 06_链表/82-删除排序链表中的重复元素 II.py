# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, head
        while q and q.next:
            if q.val == q.next.val:
                while q.next and q.val == q.next.val:
                    q = q.next
                q = q.next
                p.next = q
            else:
                p = p.next
                q = q.next
        return dummy.next


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
