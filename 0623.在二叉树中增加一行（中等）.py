"""
给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。
注意，根节点 root 位于深度 1 。

加法规则如下:
给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。
cur 原来的左子树应该是新的左子树根的左子树。
cur 原来的右子树应该是新的右子树根的右子树。

如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。
 
示例 1:
输入: root = [4,2,6,3,1,5], val = 1, depth = 2
输出: [4,1,1,2,null,null,6,3,1,5]

示例 2:
输入: root = [4,2,null,3,1], val = 1, depth = 3
输出:  [4,2,null,1,1,3,null,null,1]
 
提示:
节点数在 [1, 10^4] 范围内
树的深度在 [1, 10^4]范围内
-100 <= Node.val <= 100
-10^5 <= val <= 10^5
1 <= depth <= the depth of tree + 1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        def dfs(node, tmp_depth):
            #print(node.val, tmp_depth)
            if tmp_depth + 1 == depth:
                left_node = node.left              
                tmp_left_node = TreeNode(val)
                tmp_left_node.left = left_node
                node.left = tmp_left_node

                right_node = node.right
                tmp_right_node = TreeNode(val)
                tmp_right_node.right = right_node
                node.right = tmp_right_node
                return node
            if node.left:
                node.left = dfs(node.left, tmp_depth + 1)
            if node.right:
                node.right = dfs(node.right, tmp_depth + 1)
            return node

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            return dfs(root, 1)


        # 方法二：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if root == None:
            return
        if depth == 1:
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root


        # 方法三：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if depth == 1:
            return TreeNode(val, root, None)

        queue = [root]
        tmp_depth = 1
        while queue:
            m = len(queue)
            for _ in range(m):
                node = queue.pop(0)
                if tmp_depth + 1 == depth:
                    node.left = TreeNode(val, node.left, None)
                    node.right = TreeNode(val, None, node.right)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if tmp_depth + 1 == depth:
                return root
            tmp_depth += 1


        # 方法四：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if depth == 1:
            return TreeNode(val, root, None)
        curLevel = [root]
        for _ in range(1, depth - 1):
            tmpt = []
            for node in curLevel:
                if node.left:
                    tmpt.append(node.left)
                if node.right:
                    tmpt.append(node.right)
            curLevel = tmpt
        for node in curLevel:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root






