"""
请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。

实现 AllOne 类：
AllOne() 初始化数据结构的对象。
inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。

示例：
输入
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
输出
[null, null, null, "hello", "hello", null, "hello", "leet"]

解释
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "hello"
allOne.inc("leet");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "leet"
 
提示：
1 <= key.length <= 10
key 由小写英文字母组成
测试用例保证：在每次调用 dec 时，数据结构中总存在 key
最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10^4 次

"""


# 方法一：双向链表 + 哈希表
class Node:

    def __init__(self, key="", count=0):
        self.next = None
        self.prev = None
        self.keys = {key}   # 节点包含哪些字符串
        self.count = count  # 节点所包含字符串的计数

    def insert(self, node: 'Node') -> 'Node':  # 在self后插入node
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self):   # 从链表中移除self
        self.next.prev = self.prev
        self.prev.next = self.next

class AllOne:

    def __init__(self):
        # 初始化链表哨兵，下面判断节点的 next 若为 self.root，则表示 next 为空（prev 同理）
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root
        self.nodes = {}   # 用哈希表统计有哪些字符串

    def inc(self, key: str) -> None:
        if key not in self.nodes:   # key不在链表节点重
            if self.root.next == self.root or self.root.next.count > 1:  # 链表没有后续节点或第一个节点的统计数大于1，需要插入节点
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:    # 链表第一个节点的统计数为1
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:    # key在链表中
            cur = self.nodes[key]
            nxt = cur.next
            if nxt == self.root or nxt.count > cur.count + 1:
                self.nodes[key] = cur.insert(Node(key, cur.count + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if len(cur.keys) == 0:
                cur.remove()

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1:
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre == self.root or pre.count < cur.count - 1:
                self.nodes[key] = pre.insert(Node(key, cur.count - 1))
            else:
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if len(cur.keys) == 0:
            cur.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev != self.root else ""

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next != self.root else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


