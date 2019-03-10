# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        # 对外来说，不需要知道头结点这个属性，
        # 内部使用，不暴露所以要私有化
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def add(self,item):
        """链表头部添加元素, 头插法"""
        node = ListNode(item)
        node.next = self.__head
        self.__head = node

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            # if: cur.next!=None,会丢掉最后一个元素。
            print(cur.val, end=' ')
            cur = cur.next
        print("")

class Solution(object):
    # head是头结点，指向链表
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            while head.val==val:
                head = head.next
                if head is None:
                    return head
            pre = head
            cur = pre.next
            while cur != None:
                if cur.val == val:
                    # 删除节点的时候，pre自动的就会移动
                    pre.next=cur.next
                else:
                    # 如果没有删除节点，pre就没动
                    pre = pre.next
                cur = cur.next
            return head



if __name__ == '__main__':
    # head = 1->2->6->3->4->5->6
    ll = SingleLinkList()
    ll.add(6)
    ll.add(5)
    ll.add(4)
    ll.add(3)
    ll.add(6)
    ll.add(2)
    ll.add(1)
    ll.travel() # 1 2 6 3 4 5 6

    val = 6
    ans = Solution()
    print(ans.removeElements(ll,val))