# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None
        else:
            pre = head
            cur = head.next
            pre.next = None  # 断开一条连接线

            while cur != None:
                rear = cur.next
                cur.next = pre
                pre = cur
                cur = rear
            return pre

def main():
    head = [1,2,3,4,5]
    myresult = Solution()
    print(myresult.reverseList(head))


if __name__ == "__main__":
    main()

