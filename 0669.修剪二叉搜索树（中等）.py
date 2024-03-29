"""
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

示例 1：
输入：root = [1,0,2], low = 1, high = 2
输出：[1,null,2]

示例 2：
输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
输出：[3,2,null,1]

提示：
树中节点数在范围 [1, 10^4] 内
0 <= Node.val <= 10^4
树中每个节点的值都是 唯一 的
题目数据保证输入是一棵有效的二叉搜索树
0 <= low <= high <= 10^4

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:


        # 方法一：递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        def dfs(node):
            if not node:
                return 
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
            return node

        return dfs(root)


        # 方法二：迭代
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        while root and (root.val < low or root.val > high):
            root = root.left if root.val > high else root.right
        if not root:
            return None

        node = root
        while node.left:
            if node.left.val < low:
                node.left = node.left.right
            else:
                node = node.left

        node = root
        while node.right:
            if node.right.val > high:
                node.right = node.right.left
            else:
                node = node.right

        return root




