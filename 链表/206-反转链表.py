# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        # 第二次做,还是不会做
        dummy = ListNode(0)
        p = head.next
        dummy.next = head
        while p:
            head.next = None
            head = p
            p = p.next

    def recursive(self,head):
        if (head==None or head.next==None):
            return head
        new_head = self.recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None
        else:
            pre = head
            cur = head.next
            pre.next = None  # 断开一条连接线

            while cur != None:
                rear = cur.next
                cur.next = pre
                pre = cur
                cur = rear
            return pre

def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    myresult = Solution()
    print(myresult.reverseList(a))
    print(myresult.recursive(a))

if __name__ == "__main__":
    main()

