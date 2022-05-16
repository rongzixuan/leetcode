"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:


        # 方法一：深度优先搜索（递归）
        # 时间复杂度：O(n)，n为两棵树节点最小值
        # 空间复杂度：o(n)   
        if not root1 and not root2:
            return 

        new_root = root1 if root1 else root2

        def recursion(node1, node2, new_node):
            if not node1 and not node2:
                return 
            elif node1 and node2:    
                new_node.val = node1.val + node2.val
                new_node.left = recursion(node1.left, node2.left, new_node.left)
                new_node.right = recursion(node1.right, node2.right, new_node.right)
                return new_node
            elif node2:
                return node2
            elif node1:
                return node1

        recursion(root1, root2, new_root)

        return new_root


        # 方法二：深度优先搜索（递归）2
        # 时间复杂度：O(n)，n为两棵树节点最小值
        # 空间复杂度：o(n)
        if not root1 and not root2:
            return

        def dfs(node1, node2):
            new_node = TreeNode(-1)

            if not node1 and not root2:
                return
            elif not node2:
                return node1
            elif not node1:
                return node2
            else:                
                new_node.val = node1.val + node2.val
                new_node.left = dfs(node1.left, node2.left)
                new_node.right = dfs(node1.right, node2.right)
                return new_node

        return dfs(root1, root2)


        # 方法三：广度优先搜索（队列）
        # 时间复杂度：O(n)，n为两棵树节点最小值
        # 空间复杂度：o(n)
        if not root1 and not root2:
            return 
        elif not root1:
            return root2
        elif not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        queue = [merged]
        queue1 = [root1]
        queue2 = [root2]

        while queue1 or queue2:
            node = queue.pop(0)
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)

            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                else:
                    node.left = left2

            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                else:
                    node.right = right2

        return merged

    
