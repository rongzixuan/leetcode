"""
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
请你返回 words 数组中 一致字符串 的数目。

示例 1：
输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。

示例 2：
输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。

示例 3：
输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。

提示：
1 <= words.length <= 10^4
1 <= allowed.length <= 26
1 <= words[i].length <= 10
allowed 中的字符 互不相同 。
words[i] 和 allowed 只包含小写英文字母。

"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:


        # 方法一：哈希表 + 遍历
        # 时间复杂度：O(n * m) m为word长度
        # 空间复杂度：O(C)
        # C = 26
        n = len(words)
        ans = 0
        count = set(allowed)
        for i in range(n):
            flag = True
            for j, ch in enumerate(words[i]):
                if ch not in count:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans


        # 方法二：位运算 + 遍历
        # 时间复杂度：O(n * m) m为word长度
        # 空间复杂度：O(1)
        mask = 0
        for ch in allowed:
            mask |= 1 << (ord(ch) - ord('a'))
        #print(mask)

        ans = 0
        for word in words:
            flag = True
            for ch in word:
                if (1 << (ord(ch) - ord('a'))) & mask == 0:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans



