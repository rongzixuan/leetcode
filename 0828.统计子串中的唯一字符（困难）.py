"""
我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。
例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueChars(s) = 5 。

本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。输入用例保证返回值为 32 位整数。
注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。

示例 1：
输入: s = "ABC"
输出: 10
解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
     
示例 2：
输入: s = "ABA"
输出: 8
解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。

示例 3：
输入：s = "LEETCODE"
输出：92

提示：
1 <= s.length <= 10^5
s 只包含大写英文字符

"""

class Solution:
    def uniqueLetterString(self, s: str) -> int:


        # 方法一：数学
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        count = defaultdict(list)
        for i, ch in enumerate(s):
            count[ch].append(i)
        #print(count)

        ans = 0
        for ch, arr in count.items():
            #print(ch, arr)
            length = len(arr)
            if length== 1:
                ans += (arr[0] + 1) * (n - arr[0])
            else:
                for i, index in enumerate(arr):
                    if i == 0:
                        ans += (arr[i] + 1) * (arr[i + 1] - arr[i])
                    elif i == len(arr) - 1:
                        ans += (arr[i] - arr[i - 1]) * (n - arr[i])
                    else:
                        ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
            #print(ans)

        return ans


        # 方法二：数学
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res





