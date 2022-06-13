"""
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：
WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

"""

# 方法一：字典树 + 深度优先搜索
# 时间复杂度：
# 初始化：O(1)
# 插入：O(S)，其中S为单词的长度
# 搜索：O(26 ** S)
# 空间复杂度：O(T * 26)，其中T为所有单词的长度
class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False

    def insert(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.child[ch]:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.isEnd = True


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch != ".":
                child = node.child[ord(ch) - ord('a')]
                if child and dfs(index+1, child):
                    return True
            else:
                for child in node.child:
                    if child and dfs(index+1, child):
                        return True
            return False

        return dfs(0, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

