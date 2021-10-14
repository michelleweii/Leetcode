"""
middle 2021-10-15
"""
from functools import reduce
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = self.convertNum(l1)+self.convertNum(l2)
        sum = list(map(int,str(sum)))[::-1] # 807->[8, 0, 7]
        p = ListNode(0)
        head = p
        for i in sum:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head.next

    def convertNum(self,node):
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        # 将[2,4,3]转为243
        nums = nums[::-1]
        combine = reduce((lambda nums,y : nums*10+y),nums)
        return combine


if __name__ == '__main__':
    l1 = ListNode(2)
    a = ListNode(4)
    b = ListNode(3)
    l1.next = a
    a.next = b
    l2 = ListNode(5)
    c = ListNode(6)
    d = ListNode(4)
    l2.next = c
    c.next = d
    print(Solution().addTwoNumbers(l1,l2))