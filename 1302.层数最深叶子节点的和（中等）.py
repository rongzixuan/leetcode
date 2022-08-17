"""
给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。

示例 1：
输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15

示例 2：
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19

提示：
树中节点数目在范围 [1, 104] 之间。
1 <= Node.val <= 100

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        queue = deque([root])
        ans = 0
        while queue:
            ans = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


        # 方法二：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        max_depth = 0
        ans = 0

        def dfs(node, depth):
            nonlocal max_depth, ans
            if depth == max_depth:
                ans += node.val
            elif depth > max_depth:
                ans = node.val
                max_depth = depth
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return ans


        # 方法三：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        queue = deque([(root, 1)])
        ans = 0
        max_depth = 1
        while queue:
            for _ in range(len(queue)):
                node, depth = queue.pop()
                if depth == max_depth:
                    ans += node.val
                elif depth > max_depth:
                    ans = node.val
                    max_depth = depth
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))
        return ans



