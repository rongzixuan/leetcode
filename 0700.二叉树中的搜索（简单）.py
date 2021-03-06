"""
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2     
     / \   
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:


        # 方法一：dfs(递归)
        # 时间复杂度：O(n)
        # 空间复杂度:O(n)
        def recurve(node):
            if not node:
                return 
            elif node.val == val:
                return node
            elif node.val > val:
                return recurve(node.left)
            else:
                return recurve(node.right)

        res = recurve(root)
        return res if res else None


        # 方法二：迭代
        # 时间复杂度：O(n)
        # 空间复杂度:O(n)
        while root:
            if root.val == val:
                return root
            root = root.left if root.val > val else root.right

        return None


