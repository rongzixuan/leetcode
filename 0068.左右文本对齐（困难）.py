"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。

"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:


        # 方法一：模拟
        # 时间复杂度：O(m)， 其中m是所有字符串长度的和
        # 空间复杂度：O(m)
        def blank(k):
            return ' ' * k

        n = len(words)
        res = []
        left = right = 0      

        while True:
            left = right
            word_length = 0

            while right < n and word_length + len(words[right]) + right - left <= maxWidth:
                word_length += len(words[right])
                right += 1

            if right == n: # 到了最后一行
                s = ' '.join(words[left: ])
                res.append(s + blank(maxWidth - len(s)))
                break

            if left == right - 1: # 一行只有一个单词
                res.append(words[left] + blank(maxWidth - len(words[left])))
            else:
                #print(left, right)
                avgSpace = (maxWidth - word_length) // (right - left - 1)
                extraSpace = (maxWidth - word_length) % (right - left - 1)

                s1 = blank(avgSpace + 1).join(words[left: left + extraSpace + 1])
                s2 = blank(avgSpace).join(words[left + extraSpace + 1: right])
                res.append(s1 + blank(avgSpace) + s2)

        return res




