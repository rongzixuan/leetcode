"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        #print(root)

        # 方法一：递归(dfs)（理解错误）
        def recursion(root):
            if not root:
                return True
            if root.left:
                if root.left.val >= root.val:
                    #print('111')
                    return False
            if root.right:
                if root.right.val <= root.val:
                    #print('222')
                    return False
            if not recursion(root.left):
                #print('333')
                return False
            if not recursion(root.right):
                #print('444')
                return False
            return True

        return recursion(root)


        #方法二：递归
        def recursion(root, left, right):
            if not root:
                return True
            val = root.val
            if val <= left or val >= right:
                return False

            if not recursion(root.left, left, val):
                return False
            if not recursion(root.right, val, right):
                return False
            return True
            
        return recursion(root, -float('inf'), float('inf'))


        # 方法三：中序遍历
        stack = []
        node = root
        pre = -float('inf')

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= pre:
                return False
            pre = node.val
            node = node.right
        
        return True

    
    
