"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:


        # 方法一：迭代
        # 时间复杂度：O(m + n)，其中m、n分别为两个链表的长度
        # 空间复杂度：O(1)
        if not l1 and not l2:
            return l1
        elif not l1:
            return l2
        elif not l2:
            return l1

        if l1.val <= l2.val:
            res = l1 
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next

        tmp_node = res
        while l1 or l2:
            if not l1:
                tmp_node.next = l2
                return res
            elif not l2:
                tmp_node.next = l1
                return res
            else:
                if l1.val <= l2.val:
                    tmp_node.next = l1 
                    l1 = l1.next
                else:
                    tmp_node.next = l2
                    l2 = l2.next
                tmp_node = tmp_node.next

        return res


        # 方法二：递归
        # 时间复杂度：O(m + n)，其中m、n分别为两个链表的长度
        # 空间复杂度：O(m + n)
        if not l1 and not l2:
            return l1
        elif not l1:
            return l2
        elif not l2:
            return l1

        def recurve(tmp_node, l1, l2):
            if not l1:
                return l2
            elif not l2:
                return l1
            else:
                if l1.val <= l2.val:
                    tmp_node = l1
                    l1 = l1.next
                else:
                    tmp_node = l2
                    l2 = l2.next
                tmp_node.next = recurve(tmp_node.next, l1, l2)

            return tmp_node

        res = ListNode(-1)
        tmp = res
        return recurve(tmp, l1, l2)


        # 方法三：递归2
        # 时间复杂度：O(m + n)，其中m、n分别为两个链表的长度
        # 空间复杂度：O(m + n)
        if not l1 and not l2:
            return l1
        elif not l1:
            return l2
        elif not l2:
            return l1

        def recurve(l1, l2):
            if not l1:
                return l2
            elif not l2:
                return l1
            else:
                if l1.val <= l2.val:
                    l1.next = recurve(l1.next, l2)
                    return l1
                else:
                    l2.next = recurve(l1, l2.next)
                    return l2

            return tmp_node

        return recurve(l1, l2)


