"""
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 
提示：
节点总数在范围 [0, 10^4] 内
0 <= Node.val <= 10^4
n 叉树的高度小于或等于 1000
 
进阶：递归法很简单，你可以使用迭代法完成此题吗?

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:


        # 方法一：递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        def dfs(root):
            if not root:
                return 
            nonlocal ans
            for child in root.children:
                dfs(child)
            ans.append(root.val)

        ans = []
        dfs(root)
        return ans


        # 方法二：迭代（栈）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return 

        from collections import deque
        stack = deque()
        stack.append(root)

        ans = []
        while stack:
            root = stack.pop()
            ans.append(root.val)
            for child in root.children:
                stack.append(child)

        return ans[::-1]


        # 方法三：迭代（栈）2
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return 
            
        from collections import deque
        stack = deque()
        stack.append(root)
        ans = []
        visited = set()

        while stack:
            root = stack[-1]
            if root in visited or len(root.children) == 0:
                ans.append(root.val)
                stack.pop()
            else:
                stack.extend(reversed(root.children))
            visited.add(root)

        return ans
            





