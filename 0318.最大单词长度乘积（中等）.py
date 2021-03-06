"""
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:
输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。

示例 2:
输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。

示例 3:
输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
 
提示：
2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母

"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        # 方法一：哈希表
        # 时间复杂度：O(n * n * L)
        # 空间复杂度：O(L)
        # L为字符串最大长度
        n = len(words)

        max_length = 0
        for i in range(n-1):
            for j in range(i+1, n):
                length1, length2 = len(words[i]), len(words[j])
                hash_set = set(words[i])
                flag = True
                for k in range(length2):
                    if words[j][k] in hash_set:
                        flag = False
                if flag:
                    max_length = max(max_length, length1 * length2)

        return max_length


        # 方法二：位运算
        # 时间复杂度：O(n * n)
        # 空间复杂度：O(n * L)
        # L为字符串最大长度
        n = len(words)
        masks = [0 for _ in range(n)]

        for i in range(n):
            lenght = len(words[i])
            for j in range(lenght):
                masks[i] |= 1 << (ord(words[i][j]) - ord('a'))

        max_length = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    max_length = max(max_length, len(words[i]) * len(words[j]))

        return max_length


        # 方法三：位运算 + 哈希表
        # 时间复杂度：O(n * n)
        # 空间复杂度：O(n)
        # L为字符串最大长度
        n = len(words)
        hash_table = defaultdict(int)

        for i in range(n):
            length = len(words[i])
            mask = 0
            for j in range(length):
                mask |= 1 << (ord(words[i][j]) - ord('a'))
            if (mask in hash_table and length > hash_table[mask]) or mask not in hash_table:
                hash_table[mask] = length
        print(hash_table)

        max_length = 0
        for k1, v1 in hash_table.items():
            for k2, v2 in hash_table.items():
                if k1 & k2 == 0:
                    max_length = max(max_length, v1 * v2)

        return max_length


