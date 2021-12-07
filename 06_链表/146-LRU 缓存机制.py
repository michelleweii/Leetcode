"""
middle 2021-12-06 考察频次蛮高
https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/
1、存储 key-value 形式数据的数据结构——哈希表（字典）
2、字典本身是无序的，所以我们还需要一个类似于队列的结构来记录访问的先后顺序，这个队列需要支持如下几种操作：
    2.1、在末尾加入一项
    2.2、去除最前端一项
    2.3、将队列中某一项移到末尾（只要操作数据，就需要将数据放在最后）
"""
# 重点：双向链表删除某节点，只需要一个元素

# 定义双向链表
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# 定义LRU缓存
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # 定义哈希表，为了O(1)时间复杂度get元素
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        # 方便收尾操作元素
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到末尾，所以定义一个方法
    def move_node_to_tail(self, key):
        # 先将哈希表key指向的节点拎出来，为了简洁起名node
        node = self.hashmap[key] # 找到双向链表中，需要操作的节点的位置
        # 先删除该节点（双向链表删除节点，只需要当前指针即可实现）
        node.prev.next = node.next
        node.next.prev = node.prev
        #                 hashmap[key]                 hashmap[key]
        #                      |                            |
        #                      V        -->                 V
        # prev <-> tail  ...  node                prev <-> node <-> tail
        # 再将该节点添加到末尾, 之后将node插入到尾节点前
        # 先自己去连别人
        node.prev = self.tail.prev
        node.next = self.tail
        # 别人再来回连我
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            self.move_node_to_tail(key)
        res = self.hashmap.get(key,-1) # value是一个node，双向链表中的node
        if res == -1:
            return res
        else:
            return res.value # 获取node中的值


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到末尾
            self.move_node_to_tail(key)
        else:
            # put元素前需要记录是否超过长度，如果超过长度，需要将最早没有访问过head的元素删除，
            # 删除完了，再添加新的元素。
            if len(self.hashmap) == self.capacity:
                # 删除哈希表对应项【删除，更新哈希表】
                self.hashmap.pop(self.head.next.key)
                # 删除最久没有被访问过的节点，即头节点之后的节点（更新双向链表）
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new_node = ListNode(key,value)
            self.hashmap[key] = new_node # 【添加，更新hashmap】
            # 操作双向链表，将新添加元素接到末尾

            new_node.prev = self.tail.prev # 接前面
            new_node.next = self.tail # 接后面
            self.tail.prev.next = new_node # 接前面(完善)
            self.tail.prev = new_node # 接后面(完善)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)