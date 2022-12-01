"""
给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。
井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。

以下是井字游戏的规则：
玩家轮流将字符放入空位（' '）中。
玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。

示例 1：
输入：board = ["O  ","   ","   "]
输出：false
解释：玩家 1 总是放字符 "X" 。

示例 2：
输入：board = ["XOX"," X ","   "]
输出：false
解释：玩家应该轮流放字符。

示例 3：
输入：board = ["XXX","   ","OOO"]
输出：false

Example 4:
输入：board = ["XOX","O O","XOX"]
输出：true
 
提示：
board.length == 3
board[i].length == 3
board[i][j] 为 'X'、'O' 或 ' '
`
"""

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:


        # 方法一：模拟
        # 时间复杂度：O(C ^ 2)
        # 空间复杂度：O(1)
        #print(board[0])
        #print(board[0][1] + board[1][1] + board[2][1])
        count_X, count_O = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    count_X += 1
                elif board[i][j] == 'O':
                    count_O += 1
        #print(count_X, count_O)

        if (count_X - count_O) != 1 and (count_X - count_O) != 0:
            return False

        win_X, win_O = 0, 0
        if board[0][0] + board[1][1] + board[2][2] == 'XXX':
            win_X += 1
        elif board[0][0] + board[1][1] + board[2][2] == 'OOO':
            win_O += 1

        if board[0][2] + board[1][1] + board[2][0] == 'XXX':
            win_X += 1
        elif board[0][2] + board[1][1] + board[2][0] == 'OOO':
            win_O += 1

        for i in range(3):
            if board[i] == 'XXX':
                win_X += 1
            elif board[i] == 'OOO':
                win_O += 1

            if board[0][i] + board[1][i] + board[2][i] == 'XXX':
                win_X += 1
            elif board[0][i] + board[1][i] + board[2][i] == 'OOO':
                win_O += 1

            if win_X > 1 and count_X > 5:
                return False
            if win_O > 1 and count_O > 5:
                return False
            if win_X == 1 and win_O == 1:
                return False

        if count_X - count_O == 1 and win_O >= 1:
            return False
        if count_X == count_O and win_X >= 1:
            return False

        return True

        

            







