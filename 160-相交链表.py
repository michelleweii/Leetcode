# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def printList(self,head):
        while head:
            print(head.val,end='->')
            head = head.next
        print()


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 思路一：使用A建立一个set，遍历B，如果有元素相等，那么第一次出现的那个元素就是交点；
        # 思路二：用B的长度减去A的长度，B指针向前移动差值个元素，然后再一起遍历（这时候起点相同），遇到相同元素时，就是交点；
        self.printList(headA)
        self.printList(headB)
        skipA = self.length(headA)
        skipB = self.length(headB)


        changed = skipA-skipB
        if changed<0:
            offset = 0
            while headB and abs(changed) != offset:
                headB = headB.next
                offset += 1
        else:
            offset = 0
            while headA and abs(changed) != offset:
                headA = headA.next
                offset += 1

        while headA and headB:
            if headA.val == headB.val:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None


    def length(self,head):
        if head is None:
            return 0
        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt+=1
        return cnt


    def getIntersectionNode2(self, headA, headB):
        # 为什么这个不报错？
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        pA = headA
        pB = headB
        while pA:
            pA = pA.next
            lenA += 1
        while pB:
            pB = pB.next
            lenB += 1
        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            for i in range(lenB - lenA):
                pB = pB.next
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA
    # 原文：https: // blog.csdn.net / qq_34364995 / article / details / 80518198

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    d.next = e
    e.next = f
    f.next = b
    print(Solution().getIntersectionNode(a,d))


# 8
# [4,1,8,4,5]
# [5,0,1,8,4,5]
# 2
# 3

# Intersected at '1'（false）
# Intersected at '8'（true）
