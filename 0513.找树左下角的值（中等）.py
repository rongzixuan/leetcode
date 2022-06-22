"""
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。

示例 1:
输入: root = [2,1,3]
输出: 1

示例 2:
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
 
提示:
二叉树的节点个数的范围是 [1,10^4]
-2^31 <= Node.val <= 2^31 - 1 

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:


        # 方法一：广度优先搜索（层序遍历）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        queue = deque([(root, 0)])
        layer = 0
        ans = root.val
        while queue:
            node, tmp_layer = queue.popleft()
            if layer != tmp_layer:
                ans = node.val
                layer = tmp_layer
            if node.left:
                queue.append((node.left, tmp_layer + 1))
            if node.right:
                queue.append((node.right, tmp_layer + 1))

        return ans


        # 方法二：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        queue = deque([root])
        ans = root.val
        while queue:
            node = queue.popleft()
            ans = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)        

        return ans


        # 方法三：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        layer = 0
        ans = root.val
        def dfs(node, tmp_layer):
            nonlocal layer, ans
            if tmp_layer > layer:
                layer = tmp_layer
                ans = node.val
            if node.left:
                dfs(node.left, tmp_layer + 1)
            if node.right:
                dfs(node.right, tmp_layer + 1)

        dfs(root, layer)
        return ans


