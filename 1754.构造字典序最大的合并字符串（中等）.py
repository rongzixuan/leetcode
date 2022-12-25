"""
给你两个字符串 word1 和 word2 。你需要按下述方式构造一个新字符串 merge ：如果 word1 或 word2 非空，选择 下面选项之一 继续操作：
如果 word1 非空，将 word1 中的第一个字符附加到 merge 的末尾，并将其从 word1 中移除。
例如，word1 = "abc" 且 merge = "dv" ，在执行此选项操作之后，word1 = "bc" ，同时 merge = "dva" 。

如果 word2 非空，将 word2 中的第一个字符附加到 merge 的末尾，并将其从 word2 中移除。
例如，word2 = "abc" 且 merge = "" ，在执行此选项操作之后，word2 = "bc" ，同时 merge = "a" 。

返回你可以构造的字典序 最大 的合并字符串 merge 。

长度相同的两个字符串 a 和 b 比较字典序大小，如果在 a 和 b 出现不同的第一个位置，a 中字符在字母表中的出现顺序位于 b 中相应字符之后，就认为字符串 a 按字典序比字符串 b 更大。例如，"abcd" 按字典序比 "abcc" 更大，因为两个字符串出现不同的第一个位置是第四个字符，而 d 在字母表中的出现顺序位于 c 之后。

示例 1：
输入：word1 = "cabaa", word2 = "bcaaa"
输出："cbcabaaaaa"
解释：构造字典序最大的合并字符串，可行的一种方法如下所示：
- 从 word1 中取第一个字符：merge = "c"，word1 = "abaa"，word2 = "bcaaa"
- 从 word2 中取第一个字符：merge = "cb"，word1 = "abaa"，word2 = "caaa"
- 从 word2 中取第一个字符：merge = "cbc"，word1 = "abaa"，word2 = "aaa"
- 从 word1 中取第一个字符：merge = "cbca"，word1 = "baa"，word2 = "aaa"
- 从 word1 中取第一个字符：merge = "cbcab"，word1 = "aa"，word2 = "aaa"
- 将 word1 和 word2 中剩下的 5 个 a 附加到 merge 的末尾。

示例 2：
输入：word1 = "abcabc", word2 = "abdcaba"
输出："abdcabcabcaba"
 
提示：
1 <= word1.length, word2.length <= 3000
word1 和 word2 仅由小写英文组成

"""

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:


        # 方法一；贪心 + 双指针
        # 时间复杂度：O()
        # 空间复杂度：O(1)
        n1, n2 = len(word1), len(word2)
        ans = ""
        i, j = 0, 0
        while i < n1 and j < n2:
            #print(i, j)
            ch1, ch2 = word1[i], word2[j]
            num1, num2 = ord(ch1) - ord('a'), ord(ch2) - ord('a')
            if num1 > num2:
                ans += ch1
                i += 1
            elif num1 < num2:
                ans += ch2
                j += 1
            else:
                tmp_i, tmp_j = i, j
                while tmp_i < n1 and tmp_j < n2 and word1[tmp_i] == word2[tmp_j]:
                    tmp_i += 1
                    tmp_j += 1              
                if tmp_i < n1 and tmp_j < n2: 
                    ch1, ch2 = word1[tmp_i], word2[tmp_j]
                    num1, num2 = ord(ch1) - ord('a'), ord(ch2) - ord('a')                 
                    if num1 > num2:
                        ans += word1[i]
                        i += 1
                    elif num1 < num2:
                        ans += word2[j]
                        j += 1
                elif tmp_i == n1:
                    ch2 = word2[j]
                    ans += ch2
                    j += 1
                elif tmp_j == n2:
                    ch1 = word1[i]
                    ans += ch1
                    i += 1
        if i < n1:
            ans += word1[i:]
        if j < n2:
            ans += word2[j:]
        return ans


        # 方法二；贪心 + 双指针
        # 时间复杂度：O((n + m) * max(n, m))
        # 空间复杂度：O(1)
        merge = []
        i, j, n, m = 0, 0, len(word1), len(word2)
        while i < n or j < m:
            if i < n and word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        return ''.join(merge)



