"""
当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。比方说，"abABB" 是美好字符串，因为 'A' 和 'a' 同时出现了，且 'B' 和 'b' 也同时出现了。然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。

给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。

示例 1：
输入：s = "YazaAay"
输出："aAa"
解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。

示例 2：
输入：s = "Bb"
输出："Bb"
解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。

示例 3：
输入：s = "c"
输出：""
解释：没有美好子字符串。

示例 4：
输入：s = "dDzeE"
输出："dD"
解释："dD" 和 "eE" 都是最长美好子字符串。
由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。
 
提示：
1 <= s.length <= 100
s 只包含大写和小写英文字母。

"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:


        # 方法一：枚举
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        def check(a):
            count = set(a)
            for c in a:
                if c.lower() not in count or c.upper() not in count:
                    return False
            return True

        n = len(s)
        max_n = 0
        res = ""
        for i in range(n - 1):
            for j in range(i + 1, n):
                sub_s = s[i: j + 1]
                #print(sub_s)
                if check(sub_s) and len(sub_s) > max_n:
                    res = sub_s
                    max_n = len(sub_s)

        return res


        # 方法二：枚举2
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        n = len(s)
        max_n = 0
        res = ""
        for i in range(n):
            lower, upper = 0, 0
            for j in range(i, n):
                sub_s = s[i: j + 1]
                #print(sub_s)
                if s[j].islower():
                    lower |= (1 << (ord(s[j]) - ord('a')))
                else:
                    upper |= (1 << (ord(s[j]) - ord('A')))
                if lower == upper and len(sub_s) > max_n:
                    res = sub_s
                    max_n = len(sub_s)

        return res


        # 方法三：分治
        # 时间复杂度：O(n * C)
        # 空间复杂度：O(C)
        # C = 26
        n = len(s)
        max_index = 0
        max_length = 0

        def dfs(left, right):
            #print('left, right:', left, right)
            nonlocal max_index, max_length
            if left >= right:
                return 
            count_c = [0] * 26
            count_C = [0] * 26
            for i in range(left, right + 1):
                if s[i].isupper():
                    count_C[ord(s[i]) - ord('A')] += 1
                elif s[i].islower():
                    count_c[ord(s[i]) - ord('a')] += 1

            split = -1
            for i in range(26):
                if (count_C[i] > 0 and count_c[i] == 0) or (count_C[i] == 0 and count_c[i] > 0):
                    split = i
            #print('split:', split)
            if split == -1:
                if (right - left + 1) > max_length:
                    max_index, max_length = left, right - left + 1
                return
            if split != -1 and right - left == 1:
                return 

            i = left
            while i <= right:
                #print('i:', i)
                while i <= right and (ord(s[i].lower()) - ord('a')) == split:
                    i += 1
                if i > right:
                    break 
                start = i
                while i <= right and (ord(s[i].lower()) - ord('a')) != split:
                    i += 1
                #print('left, i - 1:', start, i - 1)
                dfs(start, i - 1)

        dfs(0, n - 1)
        return s[max_index: max_index + max_length]


        # 方法四：滑动窗口
        # 时间复杂度：O(n * C)
        # 空间复杂度：O(C)
        # C = 26
        n = len(s)
        m = len(set(s.lower()))
        #print(n, m)
        max_index, max_length = 0, 0
        for i in range(1, m + 1):      # 枚举滑动窗口内大小写同时出现的字符的个数
            count_lower = [0] * 26     # 统计小写字符
            count_upper = [0] * 26     # 统计大写字符
            left, right = 0, 0
            same = 0                   # 大小写个数都大于0个字符的个数
            total = 0                  # 出现的字符的总个数
            while right < n:
                idx = ord(s[right].lower()) - ord('a')
                if s[right].islower():
                    count_lower[idx] += 1
                    if count_lower[idx] == 1 and count_upper[idx] > 0:
                        same += 1   
                else:
                    count_upper[idx] += 1
                    if count_upper[idx] == 1 and count_lower[idx] > 0:
                        same += 1
                if count_lower[idx] + count_upper[idx] == 1:
                    total += 1

                while total > i:
                    idx = ord(s[left].lower()) - ord('a')
                    if s[left].islower():
                        count_lower[idx] -= 1
                        if count_lower[idx] == 0 and count_upper[idx] > 0:
                            same -= 1
                    else:
                        count_upper[idx] -= 1
                        if count_upper[idx] == 0 and count_lower[idx] > 0:
                            same -= 1
                    if count_lower[idx] + count_upper[idx] == 0:
                        total -= 1
                    left += 1
                    
                if same == i:
                    if right - left + 1 > max_length:
                        max_index, max_length = left, right - left + 1
                right += 1

        return s[max_index: max_index + max_length]







