# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        # 声明一个空节点
        pre = None
        cur = pHead
        while cur:
            tail = cur.next
            cur.next = pre
            pre = cur
            cur = tail
        return pre