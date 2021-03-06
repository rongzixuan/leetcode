"""
给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。

示例 1：
输入：words = ["w","wo","wor","worl", "world"]
输出："world"
解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。

示例 2：
输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply" 
 
提示：
1 <= words.length <= 1000
1 <= words[i].length <= 30
所有输入的字符串 words[i] 都只包含小写字母。

"""


class Trie:
    def __init__(self):
        self.children = [0] * 26
        self.isEnd = False
    
    def insert(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True 

    def check(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None or node.children[ch].isEnd == False:
                #print(word, 'false')
                return False
            node = node.children[ch]
        #print(word, 'true')
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:


        # 方法一：哈希集合
        # 时间复杂度：O(n * C), C = len(word)
        # 空间复杂度：O(n)
        n = len(words)
        dict1 = set()

        for i, word in enumerate(words):
            dict1.add(word)

        max_word, max_length = "", 0
        for dic in dict1:
            #print('dic:', dic)
            m = len(dic)

            flag = True
            for i in range(1, m):
                #print('dic[:i]:', dic[:i])
                if dic[:i] not in dict1:
                    flag = False
                    continue

            if flag:
                if len(dic) > max_length or (len(dic) == max_length and (max_word == "" or dic < max_word)):
                    max_word, max_length = dic, len(dic)

        return max_word


        # 方法二：排序 + 哈希集合
        # 时间复杂度：O(logn + n)
        # 空间复杂度：O(n)
        words.sort(key=lambda x: (len(x), x), reverse=False)
        #print(words)
        dict1 = set()  # 所有单词
        dict2 = set()  # 是有其他单词添加而来的单词

        max_word, max_length= "", 0
        for word in words:
            #print(word, word[:-1])
            if len(word[:-1]) == 0 or word[:-1] in dict2:
                dict2.add(word)
            if word in dict2:
                if len(word) > max_length:
                    max_word, max_length = word, len(word)           
            dict1.add(word)

        return max_word


        # 方法三：字典树
        # 时间复杂度：O()
        # 空间复杂度：O()
        trie = Trie()

        for word in words:
            trie.insert(word)

        max_word, max_length = "", 0
        for word in words:
            if trie.check(word) and (len(word) > max_length or(len(word) == max_length and word < max_word)):
                max_word, max_length = word, len(word)

        return max_word

