"""
给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，返回在甲板 board 上放置的 战舰 的数量。

战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。

 
示例 1：
输入：board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
输出：2

示例 2：
输入：board = [["."]]
输出：0
 

提示：
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 是 '.' 或 'X'

"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        # 方法一：遍历
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(1)
        m, n = len(board), len(board[0])

        res = 0
        for i, j in product(range(m), range(n)):
            #print(i, j)
            if board[i][j] == 'X':
                if (i == 0 or i > 0 and board[i-1][j] == '.') \
                and (j == 0 or j > 0 and board[i][j-1] == '.'):
                    res += 1

        return res


