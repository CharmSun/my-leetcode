#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

class LinkNode:
    def __init__(self, key, val, prev_node=None, next_node=None):
        self.key = key
        self.val = val
        self.prev = prev_node
        self.next = next_node

class DoubleLinkList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

        self.head = None
        self.tail = None
    
    def append(self, node):
        if self.size == self.capacity:
            raise ValueError("The double link list has been full.")
        self.size += 1
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
    def delete(self, node):
        if self.size == 0:
            raise ValueError("can not delete empty double link list")
        self.size -= 1

        if node == self.head:
            if node.next:
                node.next.prev = None
            self.head = node.next
        elif node == self.tail:
            if node.prev:
                node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return node
        

## 双向链表，加上hashmap
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_look_up = {}
        self.cache_list = DoubleLinkList(capacity)
        

    def get(self, key: int) -> int:
        if key not in self.cache_look_up:
            return -1
        
        node = self.cache_look_up[key]
        self.cache_list.delete(node)
        self.cache_list.append(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_look_up:
            node = self.cache_look_up[key]
            node.val = value
            self.cache_list.delete(node)
            self.cache_list.append(node)
        else:
            if self.cache_list.size == self.capacity:
                head_node = self.cache_list.delete(self.cache_list.head)
                del self.cache_look_up[head_node.key]

            new_node = LinkNode(key, value)
            self.cache_list.append(new_node)
            self.cache_look_up[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

