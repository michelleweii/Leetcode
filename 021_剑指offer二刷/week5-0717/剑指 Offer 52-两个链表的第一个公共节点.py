"""
easy 链表
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:


if __name__ == '__main__':
    listA = [2, 6, 4], listB = [1, 5]
    print(Solution().getIntersectionNode(headA, headB))