# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 思路一：使用A简历一个set，遍历B，如果有元素相等，那么第一次出现的那个元素就是交点；
        # 思路二：用B的长度减去A的长度，B指针向前移动差值个元素，然后再一起遍历（这时候起点相同），遇到相同元素时，就是交点；
