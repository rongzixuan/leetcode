"""
给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

树的 最大宽度 是所有层中最大的 宽度 。
每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。
题目数据保证答案将会在  32 位 带符号整数范围内。

示例 1：
输入：root = [1,3,2,5,3,null,9]
输出：4
解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。

示例 2：
输入：root = [1,3,2,5,null,null,9,6,null,7]
输出：7
解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。

示例 3：
输入：root = [1,3,2,5]
输出：2
解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。

提示：
树中节点的数目范围是 [1, 3000]
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        queue = [[root, 1]]
        ans = 1
        while queue:
            #print(queue)
            length = len(queue)
            #print(length)
            if length > 1:
                ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            for _ in range(length):
                node, num = queue.pop(0)
                if node.left:
                    queue.append([node.left, 2 * num])
                if node.right:
                    queue.append([node.right, 2 * num + 1])
        return ans


        # 方法二：深度优先搜索 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        min_index = defaultdict(int)
        max_index = defaultdict(int)
        ans = 1
        def dfs(node, depth, index):
            #print(node.val, depth, index)
            #print(min_index)
            #print(max_index)
            if depth not in min_index:
                min_index[depth] = index
            else:
                min_index[depth] = min(min_index[depth], index)
            if depth not in max_index:
                max_index[depth] = index
            else:
                max_index[depth] = max(max_index[depth], index)
            nonlocal ans
            ans = max(ans, max_index[depth] - min_index[depth] + 1)

            if node.left:
                dfs(node.left, depth + 1, 2 * index)
            if node.right:
                dfs(node.right, depth + 1, 2 * index + 1)

        dfs(root, 1, 1)
        return ans


        # 方法三：深度优先搜索 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        levelMin = {}
        def dfs(node: Optional[TreeNode], depth: int, index: int) -> int:
            if node is None:
                return 0
            if depth not in levelMin:
                levelMin[depth] = index  # 每一层最先访问到的节点会是最左边的节点，即每一层编号的最小值
            return max(index - levelMin[depth] + 1,
                       dfs(node.left, depth + 1, index * 2),
                       dfs(node.right, depth + 1, index * 2 + 1))
        return dfs(root, 1, 1)




