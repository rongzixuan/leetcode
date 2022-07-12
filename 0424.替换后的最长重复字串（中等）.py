"""
给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
在执行上述操作后，返回包含相同字母的最长子字符串的长度。
 
示例 1：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

示例 2：
输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
 
提示：
1 <= s.length <= 10^5
s 仅由大写英文字母组成
0 <= k <= s.length

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # 方法一：滑动窗口
        # 时间复杂度：O(C * n)
        # 空间复杂度：O(C)
        # C = 26
        n = len(s)
        total = [0] * 26

        def getCharCount(ch):
            left = 0
            count = 0
            res = 0
            for right in range(n):
                count += (1 if s[right] != ch else 0)
                while count > k:
                    count -= (1 if s[left] != ch else 0)
                    left += 1
                res = max(res, right - left + 1)
            return res

        for i in range(26):
            total[i] = getCharCount(chr(65 + i))

        #print(total)
        return max(total)


        # 方法二：滑动窗口2
        # 时间复杂度：O(n)
        # 空间复杂度：O(C)
        # C = 26
        n = len(s)
        total = [0] * 26

        left, right = 0, 0
        max_length = 0
        while right < n:
            total[ord(s[right]) - ord('A')] += 1
            max_length = max(max_length, total[ord(s[right]) - ord('A')])
            if right - left + 1 - max_length > k:
                total[ord(s[left]) - ord('A')] -= 1
                left += 1
            right += 1

        return right - left


