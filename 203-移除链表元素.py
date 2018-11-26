# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """



if __name__ == '__main__':
    # head = 1->2->6->3->4->5->6
    Node = ListNode()
    
    val = 6
    ans = Solution()
    print(ans.removeElements(head,val))