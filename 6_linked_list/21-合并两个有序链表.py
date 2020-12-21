# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        head = p
        while l1 and l2:
            if l1.val<l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2

        head = head.next
        # self.printList(head)
        return head

    def printList(self,head):
        while head:
            print(head.val)
            head = head.next

    # def getLength(self,head):
    #     length = 0
    #     while head:
    #         length += 1
    #         head=head.next
    #     return length

if __name__ == '__main__':
    l1 = ListNode(2)
    a = ListNode(3)
    b = ListNode(4)
    l1.next = a
    a.next = b
    l2 = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    l2.next = c
    c.next = d
    print(Solution().mergeTwoLists(l1,l2))
