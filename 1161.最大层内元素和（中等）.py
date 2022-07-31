"""
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

示例 1：
输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。

示例 2：
输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2
 
提示：
树中的节点数在 [1, 10^4]范围内
-10^5 <= Node.val <= 10^5

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        queue = deque([(root, 1)])
        max_sum = float('-inf')
        tmp_sum = root.val
        tmp_layer = 1
        ans = -1

        while queue:
            node, layer = queue.popleft()
            #print('node.val, layer:', node.val, layer)
            if layer == tmp_layer:
                tmp_sum += node.val
            else:
                if tmp_sum > max_sum:
                    ans = tmp_layer
                    max_sum = tmp_sum           
                tmp_sum = node.val
                tmp_layer = layer
            #print('layer, tmp_layer, tmp_sum, max_sum, ans:', layer, tmp_layer, tmp_sum, max_sum, ans)

            if node.left:
                queue.append([node.left, layer + 1])
            if node.right:
                queue.append([node.right, layer + 1])

        if tmp_sum > max_sum:
            return tmp_layer

        return ans
            




