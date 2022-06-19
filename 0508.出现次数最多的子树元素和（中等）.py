"""
给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

示例 1：
输入: root = [5,2,-3]
输出: [2,-3,4]

示例 2：
输入: root = [5,2,-5]
输出: [2]
 
提示:
节点数在 [1, 10^4] 范围内
-10^5 <= Node.val <= 10^5

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:


        # 方法一：递归（深度优先搜索）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        ans = []
        max_num = 0
        count = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            nonlocal max_num, ans, count
            res = node.val
            res += dfs(node.left)
            res += dfs(node.right)
            count[res] += 1
            if count[res] > max_num:
                ans = [res]
                max_num = count[res]
            elif count[res] == max_num:
                ans.append(res)
            #print(res)
            return res

        dfs(root)
        return ans



