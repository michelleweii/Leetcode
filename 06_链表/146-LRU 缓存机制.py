"""
middle 2021-12-02
哈希+双向链表
https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/
https://www.bilibili.com/video/BV1hp4y1x7MH
"""
# 定义双向链表
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        pass


    def put(self, key: int, value: int) -> None:
        pass



# Your LRUCache object will be instantiated and called as such:
if __name__ == '__main__':

    obj = LRUCache(capacity)
    param_1 = obj.get(key)
    obj.put(key,value)