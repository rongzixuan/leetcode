"""
一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
比方说，"abaacc" 的美丽值为 3 - 1 = 2 。

给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。

示例 1：
输入：s = "aabcb"
输出：5
解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。

示例 2：
输入：s = "aabcbaa"
输出：17
 
提示：
1 <= s.length <= 500
s 只包含小写英文字母。

"""

class Solution:
    def beautySum(self, s: str) -> int:


        # 方法一：枚举（双层循环） + 哈希表
        # 时间复杂度：O(c * n^2)
        # 空间复杂度：O(n)
        # c = 26
        ans = 0
        n = len(s)
        from collections import defaultdict
        count = defaultdict(int)
        for i in range(n):
            count = defaultdict(int)
            count[s[i]] += 1
            max_c, min_c = 1, 1
            for j in range(i + 1, n):
                count[s[j]] += 1
                min_c = min([v for k, v in count.items()])
                max_c = max([v for k, v in count.items()])
                ans += (max_c - min_c)
                #print(i, j, min_c, max_c)
        return ans










