"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:


        # 方法一：两次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next

        tmp = head
        i = 1
        while i <= count//2:
            tmp = tmp.next
            i += 1

        return tmp


        # 方法二：快慢指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


