"""
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # 方法一：深度优先搜索 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = []
        parent_node = TreeNode(-1)
        hash_table = defaultdict(list) # 记录父节点
        #print(target)


        # 找到距离target距离为k的节点
        def find_target_node(node, source, i):
            nonlocal res
            #children = fathers = [] # 节点列表 
            #child = father = node # 指针

            #print('i, taregt:', i, k) 
            #print('node:', node)
            #print('----------------')
            if not node or node == None:
                return
            elif i == k:
                res.append(node.val)
                return 

            if node.left != source:
                find_target_node(node.left, node, i+1)
            if node.right != source:
                find_target_node(node.right, node, i+1)
            if hash_table[node.val] != source:
                find_target_node(hash_table[node.val], node, i+1)


        # 深度优先搜索
        def dfs(node, parent_node):
            if not node:
                return
            if node != root:
                hash_table[node.val] = parent_node
            if node == target:
                find_target_node(node, None, 0) # 从target开始查找
                #print('hash_table:', hash_table)
            else:
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, parent_node)
        #print('hash_table:', hash_table)
        #print('~~~~~~~~~~~~~~~~~~~~~~~')
        #find_target_node(target, None, 0) # 从target开始查找
                
        return res

    
    
