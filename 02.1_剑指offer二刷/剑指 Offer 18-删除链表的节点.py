"""
easy 链表+双指针
2021-07-14
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:


if __name__ == '__main__':
    head = [4,5,1,9]
    val = 1
    print(Solution().deleteNode(head, val))
    # [4,5,9]