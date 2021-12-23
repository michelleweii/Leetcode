"""
easy 2021-12-24
https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-mo-ban-zong-jie-jian-y-dzen/
https://leetcode-cn.com/problems/palindrome-linked-list/solution/234-hui-wen-lian-biao-kuai-man-zhi-zhen-mjtur/
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):


    def isPalindrome_old(self, head):
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