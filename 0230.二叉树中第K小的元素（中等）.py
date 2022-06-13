"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MyBst:
    def __init__(self, root):
        self.root = root
        self.node_count = {}
        self.count_node_num(root)

    def count_node_num(self, node):
        if not node:
            return 0
        # 以node为根的节点数
        self.node_count[node] = 1 + self.count_node_num(node.left) + self.count_node_num(node.right)
        return self.node_count[node]

    def getNodeCount(self, node):
        return self.node_count[node] if node is not None else 0

    def getK(self, k):
        node = self.root

        while node:
            count = self.getNodeCount(node.left)
            if count == k - 1:
                return node.val
            elif count > k - 1:
                node = node.left
            else:
                node = node.right
                k -= (count + 1)
        

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        # 方法一：深度优先搜索（递归）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        from sortedcontainers import SortedList
        sl = SortedList()

        def dfs(node):
            if not node:
                return 

            if len(sl) < k:
                sl.add(node.val)
            else:
                if node.val < sl[-1]:
                    sl.pop()
                    sl.add(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        #print(sl)
        return sl[k-1]


        # 方法二：中序遍历（栈）
        # 时间复杂度：O(H+k)，其中H为二叉搜索树的深度
        # 空间复杂度：O(H)
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                #print(root.val)  # 前序遍历
                root = root.left              
            root = stack.pop()
            #print(root.val)  # 中序遍历
            k -= 1
            if k == 0:
                return root.val
            root = root.right


        # 方法三：记录子树的节点数
        # 时间复杂度：O(n)，其中n为二叉搜索树的总结点个数
        # 空间复杂度：O(n)
        bst = MyBst(root)
        return bst.getK(k)

        
