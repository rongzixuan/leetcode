"""
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:
输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2

示例 2:

输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:


        # 方法一：中序遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        stack = []
        pre = None
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre == p:
                return cur
            pre = cur
            cur = cur.right


        # 方法二：二叉搜索树
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        cur = None
        # 存在右子节点
        if p.right:
            cur = p.right
            while cur.left:
                cur = cur.left
            return cur

        # 不存在
        cur = root
        pre = None
        while cur:
            if cur.val <= p.val:
                #pre = cur
                cur = cur.right
            elif cur.val > p.val:
                pre = cur
                cur = cur.left
            
        return pre
            







