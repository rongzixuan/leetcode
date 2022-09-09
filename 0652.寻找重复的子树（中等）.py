"""
给定一棵二叉树 root，返回所有重复的子树。
对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
如果两棵树具有相同的结构和相同的结点值，则它们是重复的。

示例 1：
输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]

示例 2：
输入：root = [2,1,1]
输出：[[1]]

示例 3：
输入：root = [2,2,2,3,null,3,null]
输出：[[2,3],[3]]
 
提示：
树中的结点数在[1,10^4]范围内。
-200 <= Node.val <= 200

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:


        # 方法一：深度优先搜索 + 哈希表 + 序列化
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        count = defaultdict(int)
        ans = []
        def dfs(node):
            res1 = tuple()
            if not node.left and not node.right:
                res1 = (str(node.val), None, None)
            elif node.left and not node.right:
                res1 = (str(node.val), dfs(node.left), None)
            elif not node.left and node.right:
                res1 = (str(node.val), None, dfs(node.right))
            else:
                res1 = (str(node.val), dfs(node.left), dfs(node.right))
            #print(node.val, res1, count)
            if count[res1] == 1:
                ans.append(node)
            count[res1] += 1
            return res1

        dfs(root)
        #print(count)
        return ans


        # 方法二：深度优先搜索 + 哈希表 + 序列化
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ""
            
            serial = "".join([str(node.val), "(", dfs(node.left), ")(", dfs(node.right), ")"])
            if (tree := seen.get(serial, None)):
                repeat.add(tree)
            else:
                seen[serial] = node
            
            return serial
        
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)


        # 方法三：深度优先搜索 + 哈希表 + 序列化
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx
        
        idx = 0
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)




