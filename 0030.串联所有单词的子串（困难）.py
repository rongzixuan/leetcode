"""
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]

示例 3：
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]

提示：
1 <= s.length <= 10^4
s 由小写英文字母组成
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] 由小写英文字母组成

"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:


        # 方法一：哈希表 + 遍历
        # 时间复杂度：O(n * m)
        # 空间复杂度：O(m)
        """n = len(s)
        m = len(words)
        length = len(words[0])
        from collections import defaultdict
        candidate = defaultdict(int)
        import copy
        for i, word in enumerate(words):
            candidate[word] += 1

        ans = []
        for i in range(n):
            #print('i:', i)
            if i + m * length > n:
                return ans
            tmp_candidate = copy.deepcopy(candidate)
            #print('tmp_candidate:', tmp_candidate)
            flag = True
            for j in range(m):
                #print('s[i + j * length: i + (j + 1) * length]:', s[i + j * length: i + (j + 1) * length])
                #print('tmp_candidate:', tmp_candidate)
                if s[i + j * length: i + (j + 1) * length] in tmp_candidate and tmp_candidate[s[i + j * length: i + (j + 1) * length]] > 0:
                    #print('true:', j)
                    tmp_candidate[s[i + j * length: i + (j + 1) * length]] -= 1
                else:
                    #print('false:', j)
                    flag = False
                    break
            if flag:
                ans.append(i)

        return ans"""


        # 方法二：哈希表 + 遍历
        # 时间复杂度：O(n * m)
        # 空间复杂度：O(m)
        n = len(s)
        m = len(words)
        length = len(words[0])
        from collections import defaultdict
        candidate = defaultdict(int)
        import copy
        for i, word in enumerate(words):
            candidate[word] += 1

        ans = []
        i = 0
        visited = set()
        while i < n:
            #print('i:', i)
            tmp_i = i
            tmp_candidate = copy.deepcopy(candidate)
            while tmp_i < n:
                #print('tmp_i:', tmp_i)
                #print(visited)
                if tmp_i in visited:
                    break
                visited.add(tmp_i)               
                if tmp_i + m * length > n:
                    break               
                flag = True
                if tmp_i == i:                  
                    for j in range(m):
                        #print('s[i + j * length: i + (j + 1) * length]:', s[i + j * length: i + (j + 1) * length])
                        tmp_candidate[s[i + j * length: i + (j + 1) * length]] -= 1
                else:
                    #print(tmp_i - length,  tmp_i, tmp_i + (m - 1) * length, tmp_i + m * length)
                    #print('s[tmp_i - length: tmp_i]:', s[tmp_i - length: tmp_i])
                    #print('s[tmp_i + (m - 1) * length: tmp_i + m * length]:', s[tmp_i + (m - 1) * length: tmp_i + m * length])                   
                    tmp_candidate[s[tmp_i - length: tmp_i]] += 1
                    tmp_candidate[s[tmp_i + (m - 1) * length: tmp_i + m * length]] -= 1
                    #print('tmp_candidate:', tmp_candidate)
                for k, v in tmp_candidate.items():
                    if v != 0:
                        flag = False
                #print('flag:', flag)
                if flag:
                    ans.append(tmp_i)
                tmp_i += length
            i += 1

        #print(ans)
        return sorted(ans)


