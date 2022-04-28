"""
给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
 
示例 1：
输入：s = "owoztneoer"
输出："012"

示例 2：
输入：s = "fviefuro"
输出："45"
 
提示：
1 <= s.length <= 10^5
s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一
s 保证是一个符合题目要求的字符串

"""

class Solution:
    def originalDigits(self, s: str) -> str:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(C)，C = 10
        n = len(s)

        from collections import Counter
        c = Counter(s)
        count = [0] * 10

        count[0] = c['z']
        count[2] = c['w']
        count[4] = c['u']
        count[6] = c['x']
        count[8] = c['g']

        count[3] = c['h'] - count[8]
        count[5] = c['f'] - count[4]
        count[7] = c['s'] - count[6]

        count[1] = c['o'] - count[0] - count[2] - count[4]
        count[9] = (c['n'] - count[1] - count[7]) // 2

        #print(count)
        res = [str(i) * count[i] for i in range(10)]
        #print(res)
        return "".join(res)




