# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 环入口怎么求？
        # 快慢指针的相遇点到环入口的距离 == 链表起始点到环入口的距离

        p1 = head   # 慢指针
        p2 = head   # 快指针
        encounter = head
        flag = 0
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                # 相遇点
                encounter = p1
                flag = 1
                break
        if not flag:
            return None

        # print(encounter.val) # -4
        start = head
        pos = 0
        while start and encounter:
            if start == encounter:
                pos += 1
                # return pos # # 返回相遇节点的位置
                return start # 返回相遇点(ac)
            start = start.next
            encounter = encounter.next
        # return -1 # 返回相遇节点的位置
        return None

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(Solution().detectCycle(a))