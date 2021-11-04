"""
middle 2021-11-04
与lc108类似。
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/109-you-xu-lian-biao-zhuan-huan-er-cha-s-nrb7/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        if not head: return head
        if not head.next:  return TreeNode(head.val)
        # 利用快慢指针找到链表中点
        slow, fast = head, head
        pre = head
        while fast and fast.next:
            pre = slow
            slow, fast = slow.next, fast.next.next
        mid = slow

        root = TreeNode(mid.val)
        pre.next = None
        rhead = slow.next
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rhead)
        return root

if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedListToBST(nums))
