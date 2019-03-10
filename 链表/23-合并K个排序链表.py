# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """



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

    print(Solution().mergeKLists(a))

