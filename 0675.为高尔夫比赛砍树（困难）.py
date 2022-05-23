"""
你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：

0 表示障碍，无法触碰
1 表示地面，可以行走
比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度

每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。

你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

示例 1：
输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。

示例 2：
输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。

示例 3：
输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。
 
提示：
m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 10^9

"""


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        # 方法一：广度优先搜索
        # 时间复杂度：O(m * n * m * n)
        # 空间复杂度：O(m * n)
        m, n = len(forest), len(forest[0])

        def bfs(i, j, target):
            queue = [(i, j, 0)]
            visited = set((i, j))

            while queue:
                i, j, step = queue.pop(0)
                if forest[i][j] == target:
                    return i, j, step
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited and forest[new_i][new_j] >= 1:
                        queue.append((new_i, new_j, step + 1))
                        visited.add((new_i, new_j))
            return -1, -1, -1

        trees = sorted([forest[i][j] for i in range(m) for j in range(n) if forest[i][j] > 1])
        #print(trees)
        ans = 0
        i, j = 0, 0
        for tree in trees:
            new_i, new_j, step = bfs(i, j, tree)
            #print(tree, step)
            if step == -1:
                return -1
            ans += step
            i, j = new_i, new_j
        return ans
        
        
        
