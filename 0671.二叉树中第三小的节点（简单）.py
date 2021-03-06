"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

"""

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        # 方法一：深度优先搜索
        min_val = root.val
        second_val = float(inf)

        def dfs(root):
            nonlocal second_val
            if not root:
                return 
            elif root.val > second_val:
                return
            elif root.left and root.right:
                tmp_val = max(root.left.val, root.right.val)
                if tmp_val != min_val:
                    second_val = min(second_val, tmp_val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        #print('second_val:', second_val)
        return second_val if second_val != float(inf) else -1


        # 方法二：深度优先搜索
        min_val = root.val
        second_val = float(inf)

        def dfs(root):
            nonlocal second_val
            if not root:
                return 
            elif root.val > second_val:
                return
            else:
                if root.val != min_val:
                    second_val = min(second_val, root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        #print('second_val:', second_val)
        return second_val if second_val != float(inf) else -1


    
