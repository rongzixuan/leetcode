"""
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[[1],[3,2,4],[5,6]]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 
提示：
树的高度不会超过 1000
树的节点总数在 [0, 10^4] 之间

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return []

        from collections import deque
        queue = deque([root])

        ans = []
        while queue:
            n = len(queue)
            tmp_ans = []
            for _ in range(n):
                node = queue.popleft()
                tmp_ans.append(node.val)
                for new_node in node.children:
                    queue.append(new_node)
            ans.append(tmp_ans)

        return ans




