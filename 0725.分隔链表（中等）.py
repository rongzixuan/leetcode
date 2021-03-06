"""
给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。
这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。

返回一个由上述 k 部分组成的数组。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        count = 0
        tmp = head

        while tmp:
            count += 1
            tmp = tmp.next
        #print(count)

        if k >= count:
            avg_count = 1
            extra_count = 0
        else:
            avg_count = count // k
            extra_count = count % k
        #print("avg_count:", avg_count)
        #print("extra_count:", extra_count)

        tmp = head
        tmp_i = head
        res = []
        i = j = 0
        while i < count:           
            if i < (avg_count + 1) * extra_count:
                group_num = avg_count + 1
            else:
                group_num = avg_count
            j = 0
            tmp = tmp_i
            while j < group_num - 1:
                tmp_i = tmp_i.next
                i += 1
                j += 1
            tmp_next = tmp_i.next
            tmp_i.next = None
            tmp_i = tmp_next
            i += 1
            #print(tmp)
            res.append(tmp)

        if k >= count:
            for i in range(k - count):
                res.append(None)

        return res


   
