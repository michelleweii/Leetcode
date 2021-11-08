"""
middle 2021-11-08
链表反向双指针
https://leetcode-cn.com/problems/reorder-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-34/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:return
        p = head
        linklist = []
        # 将链表值存到 list 中, list=[1,2,3,4]
        while p:
            linklist.append(p)
            p = p.next
        # print(linklist) # [<__main__.ListNode object at 0x7f9f5f70e2d0>, <__main__.ListNode object at 0x7f9f5f727610>, <__main__.ListNode object at 0x7f9f5f72b350>, <__main__.ListNode object at 0x7f9f5f72dc50>]
        # for i in linklist:
        #     self.print_node(i)
        # 头尾指针依次取元素
        i, j = 0, len(linklist)-1
        while i<j:
            linklist[i].next = linklist[j]
            # for i in linklist:
            #     self.print_node(i)
            i += 1
            # 偶数个节点的情况，会提前相遇
            if i == j:break
            linklist[j].next = linklist[i]
            j -= 1
        linklist[i].next = None

    def print_node(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print("list:", res)

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    print(Solution().reorderList(a))