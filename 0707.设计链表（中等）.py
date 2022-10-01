"""
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：
get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 

示例：
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3

提示：
0 <= index, val <= 1000
请不要使用内置的 LinkedList 库。
get, addAtHead, addAtTail, addAtIndex 和 deleteAtIndex 的操作次数不超过 2000。

"""

# 方法一：单向链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1, None)
        self.tail = ListNode(-1, None)
        self.length = 0

    def get(self, index: int) -> int:
        #print(index, self.length)
        if self.length <= index:
            return -1
        tmp = self.head
        for i in range(index + 1):
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        index = max(0, index)
        if self.length < index:
            return 
        else:
            tmp = self.head
            for i in range(index):
                tmp = tmp.next
            nxt = tmp.next
            tmp.next = ListNode(val, None)
            tmp.next.next = nxt
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.length <= index:
            return
        else:
            tmp = self.head
            for i in range(index):
                tmp = tmp.next
            tmp.next = tmp.next.next
            self.length -= 1
        if self.length == 0:
            self.tail = self.head


# 方法二：单向链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1, None)
        self.tail = ListNode(-1, None)
        self.length = 0

    def get(self, index: int) -> int:
        #print(index, self.length)
        if self.length <= index:
            return -1
        tmp = self.head
        for i in range(index + 1):
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        #self.addAtIndex(0, val)
        if self.length == 0:
            self.tail = ListNode(val, None)
            self.head.next = self.tail
        else:
            nxt = self.head.next
            self.head.next = ListNode(val, None)
            self.head.next.next = nxt
        self.length += 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)

    def addAtTail(self, val: int) -> None:
        #self.addAtIndex(self.length, val)
        if self.length == 0:
            self.tail = ListNode(val, None)
            self.head.next = self.tail
            self.length += 1
        else:
            self.addAtIndex(self.length, val)
            #self.tail.next = ListNode(val, None)
            #self.tail = self.tail.next
        #self.length += 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)

    def addAtIndex(self, index: int, val: int) -> None:
        index = max(0, index)
        if self.length < index:
            return 
        else:
            tmp = self.head
            for i in range(index):
                tmp = tmp.next
            nxt = tmp.next
            tmp.next = ListNode(val, None)
            tmp.next.next = nxt
            self.length += 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.length <= index:
            return 
        else:
            tmp = self.head
            for i in range(index):
                tmp = tmp.next
            tmp.next = tmp.next.next
            self.length -= 1
        if self.length == 0:
            self.tail = ListNode(-1, None)


# 方法三：双向链表
class ListNode:
    def __init__(self, val=0, pre=None, nxt=None):
        self.val = val
        self.next = nxt
        self.pre = pre

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1, None)
        self.tail = ListNode(-1, None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0

    def get(self, index: int) -> int:
        #print(index, self.length)
        if self.length <= index:
            return -1
        tmp = self.head
        for i in range(index + 1):
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        #self.addAtIndex(0, val)
        if self.length == 0:
            tmp = ListNode(val, None)
            self.head.next = tmp
            tmp.pre = self.head
            self.tail.pre = tmp
            tmp.next = self.tail
        else:
            nxt = self.head.next
            tmp = ListNode(val, self.head, nxt)
            self.head.next = tmp
            nxt.pre = tmp
        self.length += 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)
        #return self.head

    def addAtTail(self, val: int) -> None:
        #self.addAtIndex(self.length, val)
        if self.length == 0:
            tmp = ListNode(val, None)
            self.head.next = tmp
            tmp.pre = self.head
            self.tail.pre = tmp
            tmp.next = self.tail
        else:
            pre = self.tail.pre
            tmp = ListNode(val, pre, self.tail)
            self.tail.pre = tmp
            pre.next = tmp
        self.length += 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)
        #return self.head

    def addAtIndex(self, index: int, val: int) -> None:
        index = max(0, index)
        if self.length < index:
            return 
        else:
            pre = self.head
            for i in range(index):
                pre = pre.next
            nxt = pre.next
            tmp = ListNode(val, pre, nxt)
            pre.next = tmp
            nxt.pre = tmp
            self.length += 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)
        #return self.head

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.length <= index:
            return 
        else:
            pre = self.head
            for i in range(index):
                pre = pre.next
            nxt = pre.next.next
            pre.next = nxt
            nxt.pre = pre
            self.length -= 1


# 方法四：双向链表
class ListNode:
    def __init__(self, val=0, pre=None, nxt=None):
        self.val = val
        self.next = nxt
        self.pre = pre

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1, None)
        self.tail = ListNode(-1, None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0

    def get(self, index: int) -> int:
        #print(index, self.length)
        if self.length <= index:
            return -1
        tmp = self.head
        for i in range(index + 1):
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)
        #return self.head

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)
        #return self.head

    def addAtIndex(self, index: int, val: int) -> None:
        index = max(0, index)
        if self.length < index:
            return 
        else:
            pre = self.head
            for i in range(index):
                pre = pre.next
            nxt = pre.next
            tmp = ListNode(val, pre, nxt)
            pre.next = tmp
            nxt.pre = tmp
            self.length += 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)
        #return self.head

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.length <= index:
            return 
        else:
            pre = self.head
            for i in range(index):
                pre = pre.next
            nxt = pre.next.next
            pre.next = nxt
            nxt.pre = pre
            self.length -= 1
        #print(self.head.next.val)
        #print(self.tail.val)
        #print('length:', self.length)
        #return self.head


# 方法五：双向链表
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        self.size -= 1
        pred.next = succ
        succ.prev = pred



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

