"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:


        # 方法一：迭代
        # 时间复杂度：O(N)
        # 空间复杂度：O(1)
        if not head:
            return head
        if not head.next:
            return head

        pre, aft = None, head
        while aft:
            tmp = aft.next
            aft.next = pre
            pre = aft
            aft = tmp

        return pre


        # 方法二：递归
        # 时间复杂度：O(N)
        # 空间复杂度：O(N)
        if not head:
            return head
        if not head.next:
            return head

        def recurve(node):
            #print('node before:', node)
            if not node or not node.next:
                return node
            res = recurve(node.next)
            node.next.next = node
            node.next = None

            #print('node after:', node)
            return res

        return recurve(head)

