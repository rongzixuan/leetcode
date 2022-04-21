"""
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

"""

class Trie:
    def __init__(self):
        #print('self1:', self)
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        #print('self2:', self)
        for c in word:
            #print('-------')
            cur = cur.children[c]
            #print('~~~~~~~')
        cur.is_word = True
        cur.word = word
        #print(cur.children)
        #print(cur.word)
        #print(cur.is_word)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # 方法一：回溯 + 字典树
        # 时间复杂度：O(m * n * 3^(l-1))
        # 空间复杂度：O(len(words) *  len(words[0]))，其中l为words中最长单词的长度
        m, n = len(board), len(board[0])
        length = len(words)
        #print(m, n, length)
        res = set()

        trie = Trie()
        for word in words:
            trie.insert(word)
        #print(trie)


        def dfs(cur, i, j):
            if board[i][j] not in cur.children:
                return 

            ch = board[i][j]
            cur = cur.children[ch]
            if cur.word != '':
                res.add(cur.word)

            board[i][j] = "#"
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < m and 0 <= new_j < n:
                    dfs(cur, new_i, new_j)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(res)







