# https://leetcode-cn.com/problems/lfu-cache/solution/chao-xiang-xi-tu-jie-dong-tu-yan-shi-460-lfuhuan-c/

class Node:
    def __init__(self, key=0, val=0, freq=0):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 头部是新节点
    def insert_node_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node=None):
        if self.is_empty():
            return
        if not node:
            node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv_map = dict()
        self.freq_map = dict()
        self.min_freq = 0 # 全局最低访问次数，删除最少使用访问次数的结点时会用到

    def _add_node(self, node):
        """
        添加node，具体操作：

        """
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList() # 创建node
        self.freq_map[node.freq].insert_node_to_head(node) # 将新node插到头部

    def _update_node(self, node, is_new_node):
        """
        更新node，具体操作：
        case1. 旧node，
            # 从旧频率哈希表中移除，如果链表为空，则频率hashmap中删除
            # 添加进新的频率哈希表
            #
        case2. 新node，
            # minfreq=1
            #
        """
        if is_new_node:
            self.min_freq = 1
            self._add_node(node)
        else:
            self.freq_map[node.freq].remove_node(node)
            if self.freq_map[node.freq].is_empty():
                del self.freq_map[node.freq]
                if node.freq == self.min_freq:
                    self.min_freq += 1
            node.freq += 1
            self._add_node(node)

    def get(self, key: int) -> int:
        if key not in self.kv_map:
            return -1
        node = self.kv_map[key]
        self._update_node(node, False) # 更新node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            node = self.kv_map[key]
            node.val = value
            self._update_node(node, False)
        else:
            # 如果初始化是个空的缓存
            if not self.capacity:
                return
            # 当容量超的时候，删除频率低+时间久的node
            if len(self.kv_map) == self.capacity:
                # 找到频率最低的双向链表
                node_to_remove = self.freq_map[self.min_freq].remove_node()
                # 如果该
                if self.freq_map[self.min_freq].is_empty():
                    del self.freq_map[self.min_freq]
                del self.kv_map[node_to_remove.key]
            node = Node(key, value, 1)
            self.kv_map[key] = node
            self._update_node(node, True)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)