"""
hard 2021-12-23 双向链表【字节常考】
（python+看图this）https://leetcode-cn.com/problems/lfu-cache/solution/chao-xiang-xi-tu-jie-dong-tu-yan-shi-460-lfuhuan-c/
https://leetcode-cn.com/problems/lfu-cache/solution/ha-xi-biao-shuang-xiang-lian-biao-java-by-liweiwei/
https://leetcode-cn.com/problems/lfu-cache/solution/pythonshuang-xiang-lian-biao-zi-dian-jian-dan-yi-d/
题目： 最不经常使用（LFU）优先访问频率高的，访问频率相同则优先最近访问的LRU，get频率高且新，然后频率++；put删掉频率最低且最久没有访问的。
"""
# 说明：本题其实就是在「力扣」第 146 题：LRU缓存机制 的基础上，在删除策略里多考虑了一个维度（「访问次数」）的信息。
# 核心思想：先考虑访问次数，在访问次数相同的情况下，再考虑缓存的时间。
# 重点：双向链表删除某节点，只需要一个元素
# 维护2个hashmap

# 定义双向链表
# 「双向链表」的尾部存储较新访问的结点，头部是当前频次最旧的结点。
# 代码按照link1实现
class Node:
    """
    双链表中的链表节点对象
    """
    def __init__(self, key=None, value=None, freq=0):
        """
        Args:
            key:对应输入的key
            value:对应输入的value
            freq:被访问的频率
            pre:指向前一个节点的指针
            next:指向后一个节点的指针
        """
        self.key = key
        self.value = value
        self.freq = freq
        # 双向链表必有
        self.prev = None
        self.next = None


class ListNode:
    """
    自定义的双向链表
    """
    def __int__(self):
        """
        Args:
            __head:双向链表的头结点
            __tail:双向链表的尾节点
        """
        self.__head = Node()
        self.__tail = Node()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head


    def insert_first_pos(self, node):
        """
        将指定的节点插入到链表的第一个位置
        Args:
            node:将要插入的节点
        """
        node.next = self.__head.next
        self.__head.next.prev = node

        node.prev = self.__head
        self.__head.next = node

    def delete_node(self, node):
        """
        从链表中删除指定的节点
        Args:
            node:将要删除的节点
        """
        # 如果链表为空
        if self.__head.next == self.__tail:return
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

    def get_last_node(self):
        """
        从链表中获取最后一个节点
        Returns:
            双向链表中的最后一个节点，如果是空链表则返回None
        """
        # 如果链表为空
        if self.__head.next == self.__tail:return None
        return self.__tail.prev

    def is_empty(self):
        """
        判断链表是否为空，除了head和tail没有其他节点即为空链表
        Returns:
            链表不空返回True，否则返回False
        """
        return self.__head.next==self.__tail

# 要维护一个minFreq的变量，用来记录LFU缓存中频率最小的元素，在缓存满的时候，可以快速定位到最小频繁的链表，以达到 O(1) 时间复杂度删除一个元素。
# 更新/查找的时候，将元素频率+1，之后如果minFreq不在频率哈希表中了，说明频率哈希表中已经没有元素了，那么minFreq需要+1，否则minFreq不变。
# 插入的时候，这个简单，因为新元素的频率都是1，所以只需要将minFreq改为1即可。
class LFUCache:
    """
    自定义的LFU缓存
    """
    def __init__(self, capacity: int):
        """
        Args:
            __capacity:缓存的最大容量
            __keymap: key->Node 这种结构的字典
            __freqmap:freq->LinkedList 这种结构的字典
            __minfreq:记录缓存中最低频率
        """
        self.__capacity = capacity
        self.__keymap = dict()  # k:node_val; v:node
        self.__freqmap = dict() # k:频率; v:是这个频率下的所有节点
        self.__minfreq = 0


    # 如果key存在，则返回对应的value，同时:
    # 将元素的访问频率+1
    # 将元素从访问频率i的链表中移除，放到频率i+1的链表中
    # 如果频率i的链表为空，则从频率哈希表中移除这个链表
    def get(self, key: int) -> int:
        """
        获取一个元素，如果key不存在则返回-1，否则返回对应的value
        同时更新被访问元素的频率
        Args:
            key:要查找的关键字
        Returns:
            如果没找到则返回-1，否则返回对应的value
        """
        if key not in self.__keymap:return -1
        # 更新频率+移到末尾「双向链表」的尾部存储较新访问的结点，头部是当前频次最旧的结点。
        node = self.__keymap[key]
        self.__increment(node)
        return node.value

    # case1. 如果key已经存在，更新node频率值
    # case2. 如果key不存在，涉及删除
    def put(self, key: int, value: int) -> None:
        """
        插入指定的key和value，如果key存在则更新value，同时更新频率
        如果key不存并且缓存满了，则删除频率最低的元素，并插入新元素
        否则，直接插入新元素
        Args:
            key:要插入的关键字
            value:要插入的值
        """
        if key in self.__keymap:
            node = self.__keymap[key]
            node.value = value #???
            self.__increment(node)
        else:
            if self.__capacity==0:
                return
            if len(self.__keymap)==self.__capacity:
                # 移除lfu
                self.__remode_min_freq_elem()
            node = Node(key, value, 1)
            self.__increment(node, True)
            self.__keymap[key] = node

    def __increment(self,node,is_new_node=False):
        """
        更新节点的访问频率
        Args:
            node:要更新的节点
            is_new_node:是否是新节点，新插入的节点和非新插入节点更新逻辑不同
        """
        if is_new_node:
            self.__minFreq = 1
            self.__set_double_linkedlist(node)
        else:
            # 如果不是新node
            self.__remode_node(node)
            node.freq += 1
            self.__set_double_linkedlist(node)
            if self.__minFreq not in self.__freqmap:
                self.__minFreq += 1

    def __set_double_linkedlist(self, node):
        """
        根据节点的频率，插入到对应的LinkedList中，如果LinkedList不存在则创建
        Args:
            node:将要插入到LinkedList的节点
        """
        if node.freq not in self.__freqmap:
            self.__freqmap[node.freq] = ListNode() # 定义一个双向链表
        linkedList = self.__freqmap[node.freq] # 将该双向链表node插入freqmap中
        linkedList.insert_first_pos(node) # 最新访问的，插入到第一个位置


    def __remode_node(self,node):
        """
        删除指定的节点，如果节点删除后，对应的双链表为空，则从__freqmap中删除这个链表
        Args:
            node:将要删除的节点
        """
        if node.freq not in self.__freqmap:
            return
        linkedList = self.__freqmap[node.freq]
        freq = node.freq
        linkedList.delete_node(node) # 双向链表删除该节点
        if linkedList.is_empty():
            del self.__freqmap[freq]

    def __remode_min_freq_elem(self):
        """
        删除频率最低的元素，从__freqmap和__keymap中都要删除这个节点，如果节点删除后对应的链表为空，则要从__freqmap中删除这个链表
        """
        linkedList = self.__freqmap[self.__minFreq]
        node = linkedList.get_last_node()
        linkedList.delete_node(node)
        del self.__keymap[node.key]
        if linkedList.is_empty():
            del self.__freqmap[node.freq]

"""
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
        self.min_freq = 0
    
    def _add_node(self, node):
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].insert_node_to_head(node)
    
    def _update_node(self, node, is_new_node):
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
        self._update_node(node, False)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            node = self.kv_map[key]
            node.val = value
            self._update_node(node, False)
        else:
            if not self.capacity:
                return
            if len(self.kv_map) == self.capacity:
                node_to_remove = self.freq_map[self.min_freq].remove_node()
                if self.freq_map[self.min_freq].is_empty():
                    del self.freq_map[self.min_freq]
                del self.kv_map[node_to_remove.key]
            node = Node(key, value, 1)
            self.kv_map[key] = node
            self._update_node(node, True)
"""

if __name__ == '__main__':

    # Your LFUCache object will be instantiated and called as such:
    # obj = LFUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)