"""
hard 2021-10-13 考察频次蛮高
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/tu-jie-kge-yi-zu-fan-zhuan-lian-biao-by-user7208t/

1、链表分区为已翻转部分+待翻转部分+未翻转部分
2、每次翻转前，要确定翻转链表的范围，这个必须通过 k 此循环来确定
3、【需记录翻转链表前驱和后继，方便翻转完成后把已翻转部分和未翻转部分连接起来】
4、【初始需要两个变量 pre 和 end，pre 代表待翻转链表的前驱，end 代表待翻转链表的末尾】注意是待翻转
5、经过k此循环，end 到达末尾，记录待翻转链表的后继 next = end.next
6、翻转链表，然后将三部分链表连接起来，然后重置 pre 和 end 指针，然后进入下一次循环
7、特殊情况，当翻转部分长度不足 k 时，在定位 end 完成后，end==null，已经到达末尾，说明题目已完成，直接返回即可
8、时间复杂度为 O(n*K)最好的情况为O(n) 最差的情况未 O(n^2)
9、空间复杂度为 O(1)除了几个必须的节点指针外，我们并没有占用其他空间

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:




if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    k = 2
    print(Solution().reverseKGroup(n1, k))