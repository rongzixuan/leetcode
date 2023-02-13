"""
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。

如果不存在这样的字符串 s ，请返回一个空字符串 ""。

示例 1：
输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。

示例 2：
输入：a = 2, b = 2, c = 1
输出："aabbc"

示例 3：
输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。
 
提示：
0 <= a, b, c <= 100
a + b + c > 0

"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:


        # 方法一：贪心
        # 时间复杂度：O(N * M * logM)
        # 空间复杂度：O(M)
        # M = 3, N = a + b + c
        count = [[a, 'a'], [b, 'b'], [c, 'c']]
        res = ""
        while True:
            count.sort(key = lambda x: x[0])
            #print('count:', count)
            #print('res:', res)
            if count[2][0] == 0:
                return res
            if not res or len(res) == 1 or res[-2] != count[2][1] or res[-1] != count[2][1]:
                res += count[2][1]
                count[2][0] -= 1
                continue
            if count[1][0] and (res[-2] != count[1][1] or res[-1] != count[1][1]):
                res += count[1][1]
                count[1][0] -= 1
                continue
            if count[0][0] and (res[-2] != count[0][1] or res[-1] != count[0][1]):
                res += count[0][1]
                count[0][0] -= 1
                continue
            else:
                return res






