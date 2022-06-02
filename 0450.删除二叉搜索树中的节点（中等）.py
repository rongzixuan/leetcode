"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。

示例 1:
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。

示例 2:
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点

示例 3:
输入: root = [], key = 0
输出: []

提示:
节点数的范围 [0, 10^4].
-10^5 <= Node.val <= 10^5
节点值唯一
root 是合法的二叉搜索树
-10^5 <= key <= 10^5
 
进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:


        # 方法一：递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        def dfs(node):
            if not node:
                return 
            if node.val == key:
                if node.left and not node.right:
                    return node.left
                elif not node.left and node.right:
                    return node.right
                elif not node.left and not node.right:
                    return None
                else:
                    pre, cur = node.left, node.left
                    while cur.right:
                        pre = cur
                        cur = cur.right
                    if pre != cur:
                        pre.right = cur.left
                        cur.left = node.left
                        cur.right = node.right
                        return cur
                    else:
                        cur.right = node.right
                        return cur
                #elif node.right:
                #    pre, cur = node.right, node.right
                #    while cur.left:
                #        pre = cur
                #        cur = cur.left
                #    if pre != cur:
                #        pre.left = None
                #        cur.left = node.left
                #        cur.right = node.right
                #        return cur
                #    else:
                #        cur.left = node.left
                #        return cur
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

        return dfs(root)


        # 方法二：迭代
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        cur, curParent = root, None
        while cur and cur.val != key:
            curParent = cur
            cur = cur.left if cur.val > key else cur.right
        if cur is None:
            return root
        if cur.left is None and cur.right is None:
            cur = None
        elif cur.right is None:
            cur = cur.left
        elif cur.left is None:
            cur = cur.right
        else:
            successor, successorParent = cur.right, cur
            while successor.left:
                successorParent = successor
                successor = successor.left
            if successorParent.val == cur.val:
                successorParent.right = successor.right
            else:
                successorParent.left = successor.right
            successor.right = cur.right
            successor.left = cur.left
            cur = successor
        if curParent is None:
            return cur
        if curParent.left and curParent.left.val == key:
            curParent.left = cur
        else:
            curParent.right = cur
        return root
      
      


