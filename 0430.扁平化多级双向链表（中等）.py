"""
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':


        # 方法一：深度优先搜索（递归）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        #print(head.val, head.prev, head.next, head.child)

        def dfs(node):
            #print(node)
            #print(node.val)
            cur = node
            last = None

            while cur:
                nxt = cur.next
                if cur.child:
                    child_last = dfs(cur.child)

                    cur.next = cur.child
                    cur.child.prev = cur

                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt
            return last

        dfs(head)    
        return head





