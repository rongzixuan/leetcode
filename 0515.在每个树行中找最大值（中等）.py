"""
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 

示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]

示例2：
输入: root = [1,2,3]
输出: [1,3]
 
提示：
二叉树的节点个数的范围是 [0,10^4]
-2^31 <= Node.val <= 2^31 - 1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return []
        queue = deque([(root, 0)])
        ans = []
        layer = 0
        max_num = root.val
        while queue:
            node, tmp_layer = queue.popleft()
            if tmp_layer > layer:
                ans.append(max_num)
                layer = tmp_layer
                max_num = node.val
            elif tmp_layer == layer:
                max_num = max(max_num, node.val)
            if node.left:
                queue.append((node.left, tmp_layer + 1))
            if node.right:
                queue.append((node.right, tmp_layer + 1))

        ans.append(max_num)
        return ans


        # 方法二：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return []

        ans = [root.val]
        def dfs(node, tmp_layer):
            #print(node.val, ans)
            if len(ans) > tmp_layer:
                if node.val > ans[tmp_layer]:
                    ans[tmp_layer] = node.val
            else:
                ans.append(node.val)
            if node.left:
                dfs(node.left, tmp_layer + 1)
            if node.right:
                dfs(node.right, tmp_layer + 1)

        dfs(root, 0)
        return ans


