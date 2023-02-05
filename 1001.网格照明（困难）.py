"""
在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。

给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。

当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。

另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj] 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。

返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。

示例 1：
输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
输出：[1,0]
解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。
第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。

示例 2：
输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
输出：[1,1]

示例 3：
输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
输出：[1,1,0]
 
提示：
1 <= n <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == 2
0 <= rowi, coli < n
queries[j].length == 2
0 <= rowj, colj < n

"""


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:


        # 方法一：哈希表（超时）
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n^2)
        from collections import defaultdict
        on1 = defaultdict(set)           # 每个格子被哪些灯照亮
        on2 = defaultdict(set)           # 每个灯照亮了哪些格子
        lamps_set = set()                # 打开的灯的集合
        #print(on1)

        for i, j in lamps:
            lamps_set.add((i, j))         
            for k in range(n):
                on1[(i, k)].add((i, j))                # 同一行
                on2[(i, j)].add((i, k))
                on1[(k, j)].add((i, j))                # 同一列
                on2[(i, j)].add((k, j))
                if 0 <= i - k < n and 0 <= j - k < n:  # 左上对角线
                    on1[(i - k, j - k)].add((i, j))
                    on2[(i, j)].add((i - k, j - k))
                if 0 <= i + k < n and 0 <= j + k < n:  # 右下对角线
                    on1[(i + k, j + k)].add((i, j))
                    on2[(i, j)].add((i + k, j + k))
                if 0 <= i - k < n and 0 <= j + k < n:  # 左下对角线
                    on1[(i - k, j + k)].add((i, j))
                    on2[(i, j)].add((i - k, j + k))
                if 0 <= i + k < n and 0 <= j - k < n:  # 右上对角线
                    on1[(i + k, j - k)].add((i, j))
                    on2[(i, j)].add((i + k, j - k))
        #print('on1:', on1)
        #print('on1[(3, 1)]:', on1[(3, 1)])

        ans = []
        for i, j in queries:
            if len(on1[(i, j)]) > 0:
                ans.append(1)
            else:
                ans.append(0)
            #on_ij = (i, j)  
            on_ij_set = set()  # 相邻9个格中是打开的灯的格子
            turn_off = False  
            for new_i, new_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j +1)]:               
                if 0 <= new_i < n and 0 <= new_j < n and (new_i, new_j) in lamps_set:
                    turn_off = True
                    on_ij_set.add((new_i, new_j))
                    lamps_set.remove((new_i, new_j))
            #print('turn_off:', turn_off)
            #print('on_ij_set:', on_ij_set)
            if turn_off:
                for on_ij in on_ij_set:
                    #print('on_ij:', on_ij)
                    for new_i, new_j in on2[on_ij]:
                        #print('new_i, new_j:', new_i, new_j)
                        on1[(new_i, new_j)].remove(on_ij)
            #print('on1:', on1)
            #print('on1[(3, 1)]:', on1[(3, 1)])

        return ans


        # 方法二：哈希表2
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        from collections import defaultdict, Counter
        lamps_set = set()
        rows, cols, diagonals, antiDiagonals = Counter(), Counter(), Counter(), Counter()

        for i, j in lamps:
            if (i, j) not in lamps_set:
                lamps_set.add((i, j))
                rows[i] += 1
                cols[j] += 1
                diagonals[i - j] += 1
                antiDiagonals[i + j] += 1

        ans = []
        for i, j in queries:
            if cols[j] or rows[i] or diagonals[i - j] or antiDiagonals[i + j]:
                ans.append(1)
            else:
                ans.append(0)
            for new_i, new_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j +1)]:               
                if 0 <= new_i < n and 0 <= new_j < n and (new_i, new_j) in lamps_set:
                    lamps_set.remove((new_i, new_j))
                    rows[new_i] -= 1
                    cols[new_j] -= 1
                    diagonals[new_i - new_j] -= 1
                    antiDiagonals[new_i + new_j] -= 1

        return ans    




