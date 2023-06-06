"""
给出二叉树的根节点 root，树上每个节点都有一个不同的值。

如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

返回森林中的每棵树。你可以按任意顺序组织答案。

示例 1：
输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]

示例 2：
输入：root = [1,2,4,null,3], to_delete = [3]
输出：[[1,2,4]]

提示：
树中的节点数最大为 1000。
每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
to_delete.length <= 1000
to_delete 包含一些从 1 到 1000、各不相同的值。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(n + m)
        # n为树节点个数，m为len(to_delete_set)
        ans = []
        to_delete_set = set(to_delete)
        def dfs(node):
            if not node:
                return None
            if node.val in to_delete_set:
                if node.left:
                    res1 = dfs(node.left)
                    if res1:
                        #print('2:', res1)
                        ans.append(res1)            
                if node.right:
                    res2 = dfs(node.right)
                    if res2:
                        #print('3:', res2)
                        ans.append(res2)   
                return None                
            else:
                res = node
                res.left = dfs(node.left)
                res.right = dfs(node.right)
                if node.val == root.val:
                    #print('1:', dfs(node.left))
                    ans.append(res)
                return res

        dfs(root)
        return ans



