


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        p1 = head # 慢指针
        p2 = head # 快指针
        # while p1 and p2:
        while p2 and p2.next:
            # 为什么这样判断可以？？
            # p2.next只是为了p2.next.next不报错
            p1 = p1.next
            p2 = p2.next.next
            # 如何判断遇见两次了呢？已解
            if p1 == p2:
                return True
        return False


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    # c = ListNode(0)
    # d = ListNode(-4)
    a.next = b
    b.next = a
    # c.next = d
    # d.next = b
    print(Solution().hasCycle(a))