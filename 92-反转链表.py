# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        pre = None
        cur = head
        i = 1
        while i < m and cur != None:
            # 其实标记一个变量的方法，对我来说可能更好理解
            pre = cur
            cur = cur.next
            # cur指向的是m所在的节点
            i += 1

        change_len = n - m + 1
        # 要记录开始反转的节点的前一个，因为要连接变换后的节点
        t1 = pre
        # 要记录开始反转的节点，因为要连接剩余的节点
        t2 = cur
        while (i <= n and cur != None):
            rear = cur.next
            cur.next = pre
            pre = cur
            cur = rear
            i += 1

        if m == 1:
            t2.next = cur
            return pre

        t2.next = cur
        t1.next = pre
        return head

if __name__ == '__main__':
