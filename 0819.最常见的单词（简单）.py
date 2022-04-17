"""
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。

题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。

 

示例：

输入: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"
解释: 
"hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"）， 
"hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
 

提示：
1 <= 段落长度 <= 1000
0 <= 禁用单词个数 <= 100
1 <= 禁用单词长度 <= 10
答案是唯一的, 且都是小写字母 (即使在 paragraph 里是大写的，即使是一些特定的名词，答案都是小写的。)
paragraph 只包含字母、空格和下列标点符号!?',;.
不存在没有连字符或者带有连字符的单词。
单词里只包含字母，不会出现省略号或者其他标点符号。

"""


import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:


        # 方法一：哈希表
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(n + m)
        # n为paragraph的长度，m为banner的个数
        new_paragraph = paragraph.replace("!", ' ').replace("?", ' ').replace(",", ' ').replace(";", ' ').replace(".", ' ').replace("'", " ")
        #print(new_paragraph)
        paragraph_list = new_paragraph.split()
        #paragraph_list = paragraph.split("! ")
        #print(paragraph_list)

        count = Counter([word.lower() for word in paragraph_list])
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        #print(count)

        banned_set = set(banned)
        for word, num in count:
            if word not in banned_set:
                return word


        # 方法二：哈希表
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(n + m)
        paragraph_list = re.split(r"[!?',;.\s]", paragraph)
        #print(paragraph_list)

        count = Counter([word.lower() for word in paragraph_list])
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        #print(count)

        banned_set = set(banned)
        banned_set.add("")
        for word, num in count:
            if word not in banned_set:
                return word















