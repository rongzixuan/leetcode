"""
所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        #print(n)
        if n < 10:
            return []

        res = set()
        from collections import defaultdict
        hash_table = defaultdict(int)

        for i in range(0, n - 10 + 1):
            tmp_s = s[i: i + 10]
            if hash_table[tmp_s]:
                hash_table[tmp_s] += 1
            else:
                hash_table[tmp_s] = 1

            if hash_table[tmp_s] > 1:
                res.add(tmp_s)

        #print(hash_table)
        return list(res)


        # 方法二：哈希表 + 滑动窗口 + 位运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        #print(n)
        if n < 10:
            return []

        x = 0
        bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for ch in s[: 10 - 1]:
            x = (x << 2) | bin[ch]
        #print(x)

        res = []
        from collections import defaultdict
        hash_table = defaultdict(int)
        for i in range(n - 10 + 1):
            x = ((x << 2) | bin[s[i + 10 - 1]]) & ((1 << 20) - 1)
            hash_table[x] += 1
            if hash_table[x] == 2:
                res.append(s[i: i + 10])

        return res

