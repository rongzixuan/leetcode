"""
设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 MagicDictionary 类：
MagicDictionary() 初始化对象
void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。 

示例：
输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]

解释
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False
 
提示：
1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] 仅由小写英文字母组成
dictionary 中的所有字符串 互不相同
1 <= searchWord.length <= 100
searchWord 仅由小写英文字母组成
buildDict 仅在 search 之前调用一次
最多调用 100 次 search

"""

# 方法一：枚举
# 时间复杂度：
# __init__(1)：
# buildDict(n)
# search(n * m)
# 空间复杂度：O(n)
# n = len(dictionary)
# m = len(searchWord)
#from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        self.dictionary = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dictionary.add(word)
        #print(self.dictionary)

    def search(self, searchWord: str) -> bool:
        for word in self.dictionary:
            #print(searchWord, word)
            m, n = len(searchWord), len(word)
            if m != n:
                continue
            else:
                if sum([1 if word[i] != searchWord[i] else 0 for i in range(n)]) == 1:
                    return True
        return False


# 方法二：字典树 + dfs
# 时间复杂度：
# __init__(1)：
# buildDict()
# search()
# 空间复杂度：O()
# n = len(dictionary)
# m = len(searchWord)
class Trie:
    def __init__(self):
        self.child = defaultdict(int)
        self.is_end = False

class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.trie
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
            cur.is_end = True
        #print('self.trie:', self.trie)

    def search(self, searchWord: str) -> bool:
        def dfs(node: Trie, index: int, count: int) -> bool:
            #print(node, index, count)
            if index == m:
                return count == 1 and node.is_end

            for ch in node.child:
                tmp_count = count
                if ch != searchWord[index]:
                    tmp_count += 1
                if dfs(node.child[ch], index + 1, tmp_count):
                    return True
            return False

        m = len(searchWord)
        return dfs(self.trie, 0, 0)


# 方法三：字典树 + dfs
class Trie:
    def __init__(self):
        self.is_finished = False
        self.child = dict()

class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
            cur.is_finished = True

    def search(self, searchWord: str) -> bool:
        def dfs(node: Trie, pos: int, modified: bool) -> bool:
            if pos == len(searchWord):
                return modified and node.is_finished
            
            ch = searchWord[pos]
            if ch in node.child:
                if dfs(node.child[ch], pos + 1, modified):
                    return True
                
            if not modified:
                for cnext in node.child:
                    if ch != cnext:
                        if dfs(node.child[cnext], pos + 1, True):
                            return True
            
            return False
        
        return dfs(self.root, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()

# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


