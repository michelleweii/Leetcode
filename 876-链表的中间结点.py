# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        count = 1
        while cur != None:
            count += 1
            cur = cur.next
        mid = (count-1) // 2 + 1
        point = 1
        cur = head
        if mid == 1:
            return head
        while cur != None:
            if point != mid:
                point += 1
                cur = cur.next
            else:
                return cur

# INPUT:[1,2,3,4,5]   RETURN: [3,4,5]
# INPUT:[1,2,3,4,5,6]   RETURN: [4,5,6]


if __name__ == '__main__':
    head = [1,2,3,4,5]