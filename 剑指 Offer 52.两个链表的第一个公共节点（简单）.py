"""
输入两个链表，找出它们的第一个公共节点。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # 方法一：双指针1
        point_i, point_j = headA, headB

        none_flag = False
        while point_i and point_j:
            if point_i == point_j:
                return point_i
            elif point_i.next == None and none_flag == True:
                return None
            
            if point_i.next:
                point_i = point_i.next
            else:
                point_i = headB
                none_flag = True

            if point_j.next:
                point_j = point_j.next
            else:
                point_j = headA


        # 方法二：双指针2
        point_i, point_j = headA, headB

        while point_i != point_j:
            point_i = point_i.next if point_i else headB
            point_j = point_j.next if point_j else headA

        return point_j




