"""
设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。

实现 WordFilter 类：
WordFilter(string[] words) 使用词典中的单词 words 初始化对象。
f(string pref, string suff) 返回词典中具有前缀 prefix 和后缀 suff 的单词的下标。如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。

示例：

输入
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]

输出
[null, 0]

解释
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e" 。
 
提示：
1 <= words.length <= 10^4
1 <= words[i].length <= 7
1 <= pref.length, suff.length <= 7
words[i]、pref 和 suff 仅由小写英文字母组成
最多对函数 f 执行 104 次调用

"""

# 方法一：哈希表
# 时间复杂度：
# __init__()
# f()
# 空间复杂度：
class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefixLength in range(1, m + 1):
                for suffixLength in range(1, m + 1):
                    self.d[word[:prefixLength] + '#' + word[-suffixLength:]] = i

    def f(self, pref: str, suff: str) -> int:
        return self.d.get(pref + '#' + suff, -1)


# 方法二：双字典树
class Trie:
    def __init__(self):
        self.children = dict()
        # self.isEnd = False
        self.indexes = list()

    def insert(self, word: str, index: int) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
            cur.indexes.append(index)
        # cur.isEnd = True

    def search(self, word: str) -> list[int]:
        cur = self
        for c in word:
            if c not in cur.children:
                return list()
            cur = cur.children[c]
        return cur.indexes


class WordFilter:
    def __init__(self, words: List[str]):
        self.head_trie = Trie()
        self.tail_trie = Trie()
        for i, word in enumerate(words):
            self.head_trie.insert(word, i)
            self.tail_trie.insert(word[::-1], i)

    def f(self, pref: str, suff: str) -> int:

        pre_index = self.head_trie.search(pref)
        suff_index = self.tail_trie.search(suff[::-1])
        m, n = len(pre_index) - 1, len(suff_index) - 1
        while m >= 0 and n >= 0 and pre_index[m] != suff_index[n]:
            if pre_index[m] > suff_index[n]:
                m -= 1
            else:
                n -= 1
        return pre_index[m] if m >= 0 and n >= 0 else -1


# 方法三：双字典树
class Trie:
    def __init__(self):
        self.child = {}
        #self.is_end = False
        self.index = list()

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie_pre, self.trie_suff = Trie(), Trie()
        for i, word in enumerate(words):
            cur = self.trie_pre
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
                cur.index.append(i)
            #cur.is_end = True   

            cur = self.trie_suff
            for ch in word[::-1]:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
                cur.index.append(i)
            #cur.is_end = True

        #print(self.trie_pre)
        #print(self.trie_suff)

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie_pre
        index1 = list()
        for ch in pref:
            #print('ch:', ch)
            if ch not in cur.child:
                index1 = list()
                break
            else:
                cur = cur.child[ch]
                index1 = cur.index

        cur = self.trie_suff
        index2 = list()
        for ch in suff[::-1]:
            if ch not in cur.child:
                index2 = list()
                break
            else:
                cur = cur.child[ch]
                index2 = cur.index

        #print('index1, index2:', index1, index2)
        m, n = len(index1), len(index2)
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0 and index1[i] != index2[j]:
            if index1[i] > index2[j]:
                i -= 1
            else:
                j -= 1
        return index1[i] if i >= 0 and j >= 0 else -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)


