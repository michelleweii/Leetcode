# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 迭代 2020/12/25 merry christmas ~
    def reverseList(self, head):
        if not head: return head
        prev = None
        cur = head
        while cur:
            tail = cur.next
            cur.next = prev
            prev = cur
            cur = tail
        return prev

    # 递归 2020/12/25
    def recursive(self, head):
        if (head == None or head.next == None):
            return head
        # new_head指向linklist尾结点
        new_head = self.recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


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

