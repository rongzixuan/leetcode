"""
有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。
对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。扩张操作定义如下：选择一个字母组（包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。

例如，以 "hello" 为例，我们可以对字母组 "o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于 3。此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得 "helllllooo"。如果 s = "helllllooo"，那么查询词 "hello" 是可扩张的，因为可以对它执行这两种扩张操作使得 query = "hello" -> "hellooo" -> "helllllooo" = s。

输入一组查询单词，输出其中可扩张的单词数量。

示例：

输入： 
s = "heeellooo"
words = ["hello", "hi", "helo"]

输出：1
解释：
我们能通过扩张 "hello" 的 "e" 和 "o" 来得到 "heeellooo"。
我们不能通过扩张 "helo" 来得到 "heeellooo" 因为 "ll" 的长度小于 3 。
 
提示：
1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s 和所有在 words 中的单词都只由小写字母组成。

"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:


        # 方法一：双指针
        # 时间复杂度：O(n*m*length)
        # 空间复杂度：O(1)
        # length = len(words)
        ans = 0
        n = len(s)
        for word in words:
            #print('word:', word)
            m = len(word)
            i, j = 0, 0
            flag = True
            count1, count2 = 1, 1
            while i < n and j < m:
                #print('i, j:', i, j)
                if s[i] != word[j]:
                    flag = False
                    break
                while i + 1 < n and s[i] == s[i + 1]:
                    #print('i, j1:', i, j)
                    count1 += 1
                    i += 1
                while j + 1 < m and word[j] == word[j + 1]:
                    #print('i, j2:', i, j)
                    count2 += 1
                    j += 1
                if s[i] != word[j]:
                    flag = False
                    break
                if (count1 >= 3 and count1 > count2) or count1 == count2:
                    count1, count2 = 1, 1
                else:
                    flag = False
                    break
                i += 1
                j += 1
            if i == n and j == m and flag:
                ans += 1
        return ans




