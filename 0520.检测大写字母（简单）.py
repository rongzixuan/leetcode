"""
我们定义，在以下情况时，单词的大写用法是正确的：
全部字母都是大写，比如 "USA" 。
单词中所有字母都不是大写，比如 "leetcode" 。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。

给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。

示例 1：
输入：word = "USA"
输出：true

示例 2：
输入：word = "FlaG"
输出：false
 
提示：
1 <= word.length <= 100
word 由小写和大写英文字母组成

"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # 方法一：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(word)
        upper_flag = False
        upper_count = 0

        for i in range(n):
            ch = word[i]
            if (ch).upper() == ch:  # 大写
                upper_count += 1
                if i == 0:
                    upper_flag = True

        #print(upper_flag, upper_count)
        if (not upper_flag and upper_count == 0) \
        or (upper_flag and upper_count == n)\
        or (upper_flag and upper_count == 1):
            return True

        return False


        # 方法二：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        return (word.upper() == word) or (word.lower() == word) or (word.title() == word)




