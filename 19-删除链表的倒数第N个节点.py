# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lenLink = self.length(head)
        print(lenLink)
        changed = lenLink-n
        cur = head
        pos = 1
        if changed == 0:
            head = head.next
            # self.printList(head)
            return head
        else:
            while cur and pos!=changed:
                rear = cur.next
                pos+=1
                cur = cur.next
            rear = cur.next
            cur.next = rear.next
            rear.next = None
            return head
            # self.printList(head)


    def printList(self,head):
        while head:
            print(head.val,end='->')
            head = head.next
        print()


    def length(self,head):
        if head is None:
            return 0
        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt+=1
        return cnt





if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    n = 5
    print(Solution().removeNthFromEnd(a,n))



