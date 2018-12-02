# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listNode = []
        cur = head
        while cur:
            listNode.append(cur.val)
            cur = cur.next
        if len(listNode)==0:
            return True
        curList = listNode[::-1]
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for i in curList:
            ptr.next = ListNode(i)
            ptr = ptr.next
        ptr = dummyRoot.next
        return ptr==head





if __name__ == '__main__':
    head = [1,2]