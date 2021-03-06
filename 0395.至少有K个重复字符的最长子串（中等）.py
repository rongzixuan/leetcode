"""
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

示例 1：
输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。

示例 2：
输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

提示：
1 <= s.length <= 10^4
s 仅由小写英文字母组成
1 <= k <= 10^5

"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:


        # 方法一：分治
        # 时间复杂度：O(n * C)
        # 空间复杂度：O(C)
        # C = 26
        n = len(s)

        def dfs(left, right):
            #print('left, right:', left, right)
            count = [0] * 26
            for i in range(left, right + 1):
                count[ord(s[i]) - ord('a')] += 1

            split = 0
            for i in range(26):
                if count[i] and count[i] < k:
                    split = chr(i + ord('a'))
                    break
            #print('split:', split)
            if split == 0:
                return right - left + 1

            i = left
            length = 0
            while i <= right:
                #print('i, split:', i, split)
                while i <= right and s[i] == split:
                    i += 1
                if i > right:
                    break
                start = i
                while i <= right and s[i] != split:
                    i += 1
                #print('start, i:', start, i)
                sub_length = dfs(start, i - 1)
                length = max(length, sub_length)
            return length 

        return dfs(0, n - 1)


        # 方法二：滑动窗口
        # 时间复杂度：O(n * C + C^2)
        # 空间复杂度：O(C)
        # C = 26
        n = len(s)
        res = 0

        for i in range(1, 27):    # 枚举滑动窗口内的字符种类个数
            left, right = 0, 0
            count = [0] * 26
            total = 0             # 滑动窗口内出现的字符的种类的个数
            less = 0              # 滑动窗口内出现的次数少于i次的字符的个数
            while right < n:
                count[ord(s[right]) - ord('a')] += 1
                if count[ord(s[right]) - ord('a')] == 1:
                    total += 1
                    less += 1
                if count[ord(s[right]) - ord('a')] == k:
                    less -= 1
                while total > i:
                    count[ord(s[left]) - ord('a')] -= 1
                    if count[ord(s[left]) - ord('a')] == k - 1:
                        less += 1
                    if count[ord(s[left]) - ord('a')] == 0:
                        total -= 1
                        less -= 1
                    left += 1
                if less == 0:
                    res = max(res, right - left + 1)
                right += 1

        return res
                

