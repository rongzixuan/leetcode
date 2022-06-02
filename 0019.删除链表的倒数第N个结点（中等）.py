"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:


        # 方法一：两次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        dummy_node = ListNode(0, head)
        tmp = dummy_node
        count = -1

        while tmp:
            count += 1
            tmp = tmp.next
        #print('count:', count)

        tmp = dummy_node
        for i in range(count - n):
            tmp = tmp.next

        tmp.next = tmp.next.next
        return dummy_node.next


        # 方法二：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        dummy_node = ListNode(0, head)

        slow = fast = dummy_node
        for i in range(n+1):
            fast = fast.next
        #print(fast)

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy_node.next

