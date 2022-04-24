"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:


        # 方法一：数组
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        a = []

        tmp = head
        while tmp:
            a.append(tmp)
            tmp = tmp.next
        #print(a)

        return a[-k]


        # 方法二：两次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        count = 0
        tmp = head
        i = 0

        while tmp:
            count += 1
            tmp = tmp.next
        #print(count)

        tmp = head
        while i <= count:
            if i == count - k:
                return tmp
            tmp = tmp.next
            i += 1


        # 方法三：双指针（快慢指针）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        fast = slow = head
        i = 0

        while i < k:
            fast = fast.next
            i += 1
        #print('fast:', fast)

        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow





