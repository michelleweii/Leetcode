"""
easy 2020/12/25 链表
归并排序合并过程
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        p = ListNode(-1) # 虚拟头节点
        head = p
        while list1 and list2:
            if list1.val<list2.val:
                p.next = list1
                list1 = list1.next # 原链表指针更新
                p = p.next # 新链表指针更新
            else:
                p.next = list2
                list2 = list2.next
                p = p.next
        if list1: p.next = list1
        if list2: p.next = list2

        return head.next

    def printList(self,head):
        while head:
            print(head.val)
            head = head.next

if __name__ == '__main__':
    list1 = ListNode(2)
    a = ListNode(3)
    b = ListNode(4)
    list1.next = a
    a.next = b
    list2 = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    list2.next = c
    c.next = d
    print(Solution().mergeTwoLists(list1,list2))
