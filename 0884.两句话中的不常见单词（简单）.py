"""
句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。

如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。

给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。

示例 1：
输入：s1 = "this apple is sweet", s2 = "this apple is sour"
输出：["sweet","sour"]

示例 2：
输入：s1 = "apple apple", s2 = "banana"
输出：["banana"]

提示：
1 <= s1.length, s2.length <= 200
s1 和 s2 由小写英文字母和空格组成
s1 和 s2 都不含前导或尾随空格
s1 和 s2 中的所有单词间均由单个空格分隔

"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:


        # 方法一：哈希表
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(m + n)
        m, n = len(s1), len(s2)
        from collections import defaultdict
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for c1 in s1.split(' '):
            count1[c1] += 1
        #print(count1)

        ans = []
        for c2 in s2.split(' '):
            count2[c2] += 1   

        for k, v in count1.items():
            if v == 1 and count2[k] == 0:
                ans.append(k)  
        for k, v in count2.items():
            if v == 1 and count1[k] == 0:
                ans.append(k)          

        return ans


        # 方法二：哈希表2
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(m + n)
        m, n = len(s1), len(s2)
        from collections import Counter
        count = Counter(s1.split()) + Counter(s2.split()) 

        ans = []
        for k, v in count.items():
            if v == 1:
                ans.append(k)           

        return ans

    
    
    
