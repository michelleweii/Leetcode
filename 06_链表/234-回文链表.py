# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        listNode = []
        cur = head
        while cur:
            listNode.append(cur.val)
            cur = cur.next
        if len(listNode) == 0:
            return True
        curList = listNode[::-1]
        return curList == listNode


if __name__ == '__main__':
    head = [1,2]