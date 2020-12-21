# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        # 第二次做,还是不会做
        # 迭代
        if (head is None) or (head.next is None):
            return head
        p1 = head
        p2 = p1.next
        p3 = p2.next
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        head.next = None
        head = p1
        return head


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
            pre.next = None   #最开始的头节点要变成尾节点，即在后面补null使链表终结
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

