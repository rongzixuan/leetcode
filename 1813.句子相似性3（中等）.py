"""
一个句子是由一些单词与它们之间的单个空格组成，且句子的开头和结尾没有多余空格。比方说，"Hello World" ，"HELLO" ，"hello world hello world" 都是句子。每个单词都 只 包含大写和小写英文字母。

如果两个句子 sentence1 和 sentence2 ，可以通过往其中一个句子插入一个任意的句子（可以是空句子）而得到另一个句子，那么我们称这两个句子是 相似的 。比方说，sentence1 = "Hello my name is Jane" 且 sentence2 = "Hello Jane" ，我们可以往 sentence2 中 "Hello" 和 "Jane" 之间插入 "my name is" 得到 sentence1 。

给你两个句子 sentence1 和 sentence2 ，如果 sentence1 和 sentence2 是相似的，请你返回 true ，否则返回 false 。

示例 1：
输入：sentence1 = "My name is Haley", sentence2 = "My Haley"
输出：true
解释：可以往 sentence2 中 "My" 和 "Haley" 之间插入 "name is" ，得到 sentence1 。

示例 2：
输入：sentence1 = "of", sentence2 = "A lot of words"
输出：false
解释：没法往这两个句子中的一个句子只插入一个句子就得到另一个句子。

示例 3：
输入：sentence1 = "Eating right now", sentence2 = "Eating"
输出：true
解释：可以往 sentence2 的结尾插入 "right now" 得到 sentence1 。

示例 4：
输入：sentence1 = "Luky", sentence2 = "Lucccky"
输出：false

提示：
1 <= sentence1.length, sentence2.length <= 100
sentence1 和 sentence2 都只包含大小写英文字母和空格。
sentence1 和 sentence2 中的单词都只由单个空格隔开。

"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:


        # 方法一：双指针
        # 时间复杂度：O(n1 + n2)
        # 空间复杂度：O(n1 + n2)
        if sentence1 == sentence2:
            return True
        n1, n2 = len(sentence1), len(sentence2)
        if n1 < n2:
            sentence1, sentence2 = sentence2, sentence1
            n1, n2 = n2, n1
        #print(sentence1, sentence2)
        arr1, arr2 = sentence1.split(' '), sentence2.split(' ')
        m1, m2 = len(arr1), len(arr2)
        if m1 < m2:
            return False

        if arr1[:m2] == arr2:
            #print(sentence1[:n2])
            #print('true1')
            return True
        elif arr1[m1 - m2:] == arr2:
            #print(sentence1[n1 - n2: ])
            #print('true1')
            return True
        else:
            i, j = 0, 0
            index = 0
            while i < m1 and j < m2 and arr1[i] == arr2[j]:
                i += 1
                j += 1
            if i == 0 or j == 0:
                #print('false1')
                return False
            index = i - 1
            #while i < m1 and j < m2 and arr1[i] != arr2[j]:
            #    i += 1
            #if i == m1:
            #    #print('false2')
            #    return False
            i, j = m1 - m2 + j, j
            while i < m1 and j < n2 and arr1[i] == arr2[j]:
                i += 1
                j += 1
            if i < m1 or j < m2:
                #print('false3')
                return False
            #print('true3')
            return True


        # 方法二：双指针
        # 时间复杂度：O(n1 + n2)
        # 空间复杂度：O(n1 + n2)
        words1, words2 = sentence1.split(), sentence2.split()
        m, n = len(words1), len(words2)
        if m < n:
            words1, words2 = words2, words1
            m, n = n, m
        i = j = 0
        while i < n and words1[i] == words2[i]:
            i += 1
        while j < n and words1[m - 1 - j] == words2[n - 1 - j]:
            j += 1
        return i + j >= n



            

