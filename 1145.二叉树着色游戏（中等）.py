"""
有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。

最开始时：
「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）；
「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。

「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。

之后两位玩家轮流进行操作，「一号」玩家先手。每一回合，玩家选择一个被他染过色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色（「一号」玩家染红色，「二号」玩家染蓝色）。

如果（且仅在此种情况下）当前玩家无法找到这样的节点来染色时，其回合就会被跳过。

若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。

现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true ；若无法获胜，就请返回 false 。

示例 1 ：
输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：true
解释：第二个玩家可以选择值为 2 的节点。

示例 2 ：
输入：root = [1,2,3], n = 3, x = 1
输出：false
 
提示：
树中节点数目为 n
1 <= x <= n <= 100
n 是奇数
1 <= Node.val <= n
树中所有值 互不相同

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        """
        我们先通过DFS，找到「一号」玩家着色点x  所在的节点，记为 node,
        接下来，我们统计 node 的左子树、右子树的节点个数，分别记为 l 和 r，而 
        node 父节点方向上的个数为 n−l−r−1。只要满足 
        max(l,r,n−l−r−1) > 2 ，则「二号」玩家存在一个必胜策略。
        """
        #print(root)
        def getCount(node):
            if not node:
                return 0
            return 1 + (getCount(node.left) + getCount(node.right))

        def dfs(node):
            #print('node:', node)
            if not node or node.val == x:
                return node            
            else:
                res1 = dfs(node.left)
                res2 = dfs(node.right)
                return res1 or res2

        node = dfs(root)
        #print(node)
        left = getCount(node.left)
        right = getCount(node.right)
        return max(left, right, n - left - right - 1) > n / 2





