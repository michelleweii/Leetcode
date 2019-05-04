# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = head
        cur = pre.next
        while cur != None:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = pre.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    a.next = b
    b.next = c
    print(Solution().deleteDuplicates(a))
