"""
给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局 。构造此格式化布局矩阵需要遵循以下规则：
树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。

矩阵的列数 n 应该等于 2height+1 - 1 。

根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。

对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2height-r-1] ，右子节点放置在 res[r+1][c+2height-r-1] 。
继续这一过程，直到树中的所有节点都妥善放置。

任意空单元格都应该包含空字符串 "" 。

返回构造得到的矩阵 res 。

示例 1：
输入：root = [1,2]
输出：
[["","1",""],
 ["2","",""]]
 
示例 2：
输入：root = [1,2,3,null,4]
输出：
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]

提示：
树中节点数在范围 [1, 2^10] 内
-99 <= Node.val <= 99
树的深度在范围 [1, 10] 内

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        max_depth = 0
        def dfs1(node, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            if node.left:
                dfs1(node.left, depth + 1)
            if node.right:
                dfs1(node.right, depth + 1)
        dfs1(root, 1)

        m, n = max_depth, 2**max_depth - 1
        ans = [[""] * n for _ in range(m)]
        #ans[0][(n - 1) // 2] = str(root.val)
        #print(ans)

        def dfs2(node, depth, index):
            #print(depth, index)
            ans[depth - 1][index] = str(node.val)
            if node.left:
                dfs2(node.left, depth + 1, index - 2**(m - 1 - depth))
            if node.right:
                dfs2(node.right, depth + 1, index + 2**(m - 1 - depth))
        dfs2(root, 1, (n - 1) // 2)

        return ans


        # 方法二：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        max_depth = 0
        queue1 = [(root, 1)]
        while queue1:
            #print('queueq1:', queue1)
            node, depth = queue1.pop(0)
            #print(node.val, depth)
            max_depth = max(max_depth, depth)
            if node.left:
                queue1.append((node.left, depth + 1))
            if node.right:
                queue1.append((node.right, depth + 1))

        m, n = max_depth, 2**max_depth - 1
        ans = [[""] * n for _ in range(m)]
        #ans[0][(n - 1) // 2] = str(root.val)
        #print(ans)

        queue1 = [(root, 1, (n - 1) // 2)]
        while queue1:
            node, depth, index = queue1.pop(0)
            ans[depth - 1][index] = str(node.val)
            if node.left:
                queue1.append((node.left, depth + 1, index - 2**(m - 1 - depth)))
            if node.right:
                queue1.append((node.right, depth + 1, index + 2**(m - 1 - depth)))

        return ans




