"""
请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 方法一：遍历 + 哈希表
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        from collections import defaultdict
        hash_table = defaultdict(list)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    left = j//3*3
                    right = j//3*3 + 2
                    up = i//3*3
                    down = i//3*3 + 2
                    #print('i, j, left, right, up, down:', i, j, left, right, up, down)                  
                    nums = hash_table[num]
                    for new_i, new_j in nums:
                        #print('i, j, new_i, new_j:', i, j, new_i, new_j)
                        if new_i == i or new_j == j:
                            return False
                        if left <= new_j <= right and up <= new_i <= down:
                            return False
                    hash_table[num].append((i, j))

        return True



    
