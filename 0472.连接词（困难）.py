"""
给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。

连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。


示例 1：
输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
     
示例 2：
输入：words = ["cat","dog","catdog"]
输出：["catdog"]
 

提示：
1 <= words.length <= 10^4
0 <= words[i].length <= 1000
words[i] 仅由小写字母组成
0 <= sum(words[i].length) <= 10^5

"""


# 方法一：字典树 + 深度优先搜索（递归）
# 时间复杂度：
# 空间复杂度：
class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False

    def insert(self, word):
        #print(word)
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.child[ch]:
                node.child[ch] = Trie()
            node = node.child[ch]
        node.isEnd = True 

    def dfs(self, word, index):
        if index == len(word):
            return True
        node = self
        for i in range(index, len(word)):
            ch = ord(word[i]) - ord('a')
            node = node.child[ch]
            if node is None:
                return False
            if node.isEnd and self.dfs(word, i + 1):
                return True
        return False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        #print(words)
        root = Trie()

        res = []
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0):
                res.append(word)
            else:
                root.insert(word)

        return res



