"""
给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。
两个节点之间的路径长度 由它们之间的边数表示。

示例 1:
输入：root = [5,4,5,1,1,5]
输出：2

示例 2:
输入：root = [1,4,5,4,4,5]
输出：2

提示:
树的节点数的范围是 [0, 10^4] 
-1000 <= Node.val <= 1000
树的深度将不超过 1000

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return 0
        ans = 0

        def dfs(node):
            nonlocal ans
            length = 0
            length1, length2 = 0, 0
            if node.left:
                left = dfs(node.left)
                if node.val == node.left.val:
                    length1 = left + 1
                    length += length1                  
            if node.right:
                right = dfs(node.right)
                if node.val == node.right.val:
                    length2 = right + 1
                length += length2            
            ans = max(ans, length)
            #print('node.val, length, length1, length2, ans:', node.val, length, length1, length2, ans)
            return max(length1, length2)

        length = dfs(root)
        return ans





