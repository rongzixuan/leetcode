"""
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

示例 1:
输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

输出: "1(2(4))(3)"
解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。

示例 2:
输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

输出: "1(2()(4))(3)"
解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:


        # 方法一：递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return ""

        ans = ""

        def dfs(root):
            nonlocal ans
            ans += str(root.val)
            if root.left and root.right:
                ans += '('
                dfs(root.left)
                ans += ')'
                ans += '('
                dfs(root.right)
                ans += ')'
            elif root.left:
                ans += '('
                dfs(root.left)
                ans += ')'
            elif root.right:
                ans += '('
                ans += ')'
                ans += '('
                dfs(root.right)
                ans += ')'

        dfs(root)
        return ans


        # 方法二：迭代（栈）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return ""

        ans = ""
        stack = [root]
        visited = set()
        while stack:
            node = stack[-1]
            if node in visited:
                ans += ')'
                stack.pop()
            else:
                visited.add(node)
                ans += ('(' + str(node.val))

                if node.left and node.right:
                    stack.append(node.right)
                    stack.append(node.left)
                elif node.left:
                    stack.append(node.left)
                elif node.right:
                    ans += '()'
                    stack.append(node.right)

        return ans[1: -1]




