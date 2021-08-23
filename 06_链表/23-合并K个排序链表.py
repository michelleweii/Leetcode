# Definition for singly-linked list.
# 思路：
# 先把整个链表拉成一个链表，把这个链表的值全部存储在列表中，再将列表排序，新建一个链表重新一个一个指向列表的每一项
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue
from heapq import heappush,heappop
class Solution(object):
    def mergeKLists(self, lists):
        dummy = curr = ListNode(None)
        q = PriorityQueue()
        for idx,node in enumerate(lists):
            # 我的妈，链表竟然可以这样遍历
            # print(idx,node) # TypeError: 'ListNode' object is not iterable
            # 不可以这样遍历- -
            if node:
                q.put((node.val,idx,node))
        # print(q.get()) # (1, 0, <__main__.ListNode object at 0x105d20518>)
        while not q.empty():
            # 最小的元素在链表尾部
            _,idx,curr.next = q.get()
            curr = curr.next
            if curr.next:q.put((curr.next.val,idx,curr.next))
        return dummy.next

    ## using minheap
    def mergeKLists2(self, lists):
        dummy = curr = ListNode(None)
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx, node))

        while heap:
            _, idx, curr.next = heappop(heap)
            curr = curr.next
            if curr.next:
                heappush(heap, (curr.next.val, idx, curr.next))
        return dummy.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(5)

    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)

    g = ListNode(2)
    h = ListNode(6)

    a.next = b
    b.next = c
    d.next = e
    e.next = f
    g.next = h

    lists = [a,d,g]
    print(Solution().mergeKLists(lists))
