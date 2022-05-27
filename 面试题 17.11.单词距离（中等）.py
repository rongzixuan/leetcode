"""
有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：
输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1

提示：
words.length <= 100000

"""

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:


        # 方法一：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        index1, index2 = -1, -1
        ans = 10 ** 7
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                ans = min(ans, abs(index1 - index2))
        return ans

        
