"""
middle 2021-11-02
对链表升序且O(n log n)，回顾下nlogn的排序有哪些？
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if not head:return head





if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    print(Solution().sortList(a))