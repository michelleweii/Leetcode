"""
medium 2021-10-14
反转链表
这里翻转用了3个指针，pre、cur、post
同样反转链表有92、206【反转链表必考！】
https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-lian-r063e/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 如果没有节点or只有一个节点
        if not head or not head.next: return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 循环，必须要有pre.next和pre.next.next，否则交换结束
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre，cur，post对应最左，中间的，最右边的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return dummy.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(Solution().swapPairs(n1))