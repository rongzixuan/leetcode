"""
给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。

对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。

二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。

返回二叉树的 垂序遍历 序列。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        # 方法一：哈希表 + dfs（递归）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        hash_table = defaultdict(list)
        res = []

        # 深度优先搜索
        def dfs(node, depth, column):
            if not node:
                return
            hash_table[node] = (column, depth, node.val)
            dfs(node.left, depth+1, column-1)
            dfs(node.right, depth+1, column+1)

        dfs(root, 0, 0)
        #print('hash_table1:', hash_table)
        hash_list = sorted(hash_table.items(), key=lambda x:x[1]) # 按列编号、行编号、值排序
        #print('hash_list:', hash_list)

        # 存入res
        n = len(hash_list)
        i = 0
        while i < n:
            tmp_res = []
            tmp_val = hash_list[i][1][0] # 列编号
            tmp_res.append(hash_list[i][0].val) # 节点的值
            j = i + 1
            if j < n and hash_list[j][1][0] == tmp_val:
                while j < n and hash_list[j][1][0] == tmp_val: # 比较列编号
                    tmp_res.append(hash_list[j][0].val)
                    j += 1
                i = j
            else:
                i += 1
            res.append(tmp_res)
        #print('res:', res)
        return res



        # 方法二：哈希表 + dfs（递归）2
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)

        node_list = []
        res = []

        def dfs(node, col, depth):
            if not node:
                return 
            
            node_list.append((col, depth, node.val))
            dfs(node.left, col-1, depth+1)
            dfs(node.right, col+1, depth+1)

        dfs(root, 0, 0)
        node_list.sort()
        #print('node_list:', node_list)

        last_col = float('-inf')
        for i in range(len(node_list)):
            if last_col == node_list[i][0]:
                res[-1].append(node_list[i][2])
                
            else:
                res.append([node_list[i][2]])
            last_col = node_list[i][0] # 列

        return res



        # 方法三：哈希表 + dfs（栈）(前序遍历)
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        stack = []
        node_list = []
        res = []
        node = root
        depth = col = 0

        while node or stack:
            while node:
                node_list.append((col, depth, node.val))
                stack.append((col, depth, node))
                node = node.left
                col -= 1
                depth += 1
            col, depth, node = stack.pop()
            node = node.right
            col += 1
            depth += 1

        #print(node_list)
        node_list.sort()
        #print(node_list)

        n = len(node_list)
        last_col = float('-inf')
        for i in range(n):
            if last_col == node_list[i][0]: # 列
                res[-1].append(node_list[i][2]) # 节点值
            else:
                res.append([node_list[i][2]])
            last_col = node_list[i][0]

        return res



        # 方法四：哈希表 + bfs（队列）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        res = []
        node_list = []
        col = depth = 0
        queue = [(col, depth, root)]

        while queue:
            col, depth, node = queue.pop(0)
            #print('node:', node)
            node_list.append((col, depth, node.val))

            if node.left:
                queue.append((col-1, depth+1, node.left))
            if node.right:
                queue.append((col+1, depth+1, node.right))

        #print('node_list:', node_list)
        node_list.sort()

        n = len(node_list)
        last_col = float('-inf')
        for i in range(n):
            if last_col == node_list[i][0]: # 列
                res[-1].append(node_list[i][2]) # 节点值
            else:
                res.append([node_list[i][2]])
            last_col = node_list[i][0]

        return res




