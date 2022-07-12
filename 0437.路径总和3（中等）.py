"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        
        # 方法一：深度优先搜索
        # 时间复杂度：O(n * depth)
        # 空间复杂度：O(n)
        sum_list = [0]

        def dfs(node, tmp_sum, sum_list):
            global res
            #print('res:', res)
            if not node:
                return 0

            res = 0
            tmp_sum += node.val
            #print('tmp_sum:', tmp_sum)

            #print('sum_list before:', sum_list)            
            for father_sum in sum_list:
                if tmp_sum - father_sum == targetSum:
                    res += 1

            #print('res:', res)
            sum_list.append(tmp_sum)
            #print('sum_list after:', sum_list)

            res += dfs(node.left, tmp_sum, sum_list)
            res += dfs(node.right, tmp_sum, sum_list)
            sum_list.pop(-1)
            return res

        res = dfs(root, 0, sum_list)
        return res


        # 方法二：深度优先搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)，栈的开销
        def dfs(node, targetSum):
            if not node:
                return 0

            res = 0
            if node.val == targetSum:
                res += 1
            res += dfs(node.left, targetSum - node.val)
            res += dfs(node.right, targetSum - node.val)
            return res

        if not root:
            return 0

        res = dfs(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res


        # 方法三：前缀和
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        from collections import defaultdict
        pre_sum = defaultdict(int)
        pre_sum[0] = 1

        def dfs(node, targetSum, tmp_sum):
            if not node:
                return 0

            res = 0
            tmp_sum += node.val
            #print('tmp_sum:', tmp_sum)
            #print('pre_sum before:', pre_sum)
            res += pre_sum[tmp_sum - targetSum]
            pre_sum[tmp_sum] += 1
            #print('pre_sum after:', pre_sum)

            res += dfs(node.left, targetSum, tmp_sum)
            res += dfs(node.right, targetSum, tmp_sum)

            pre_sum[tmp_sum] -= 1
            return res

        res = dfs(root, targetSum, 0)
        return res



    
    
