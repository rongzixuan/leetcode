"""
我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。
原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。
最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。
 
示例 1:
输入: "(123)"
输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

示例 2:
输入: "(00011)"
输出:  ["(0.001, 1)", "(0, 0.011)"]
解释: 
0.0, 00, 0001 或 00.01 是不被允许的。

示例 3:
输入: "(0123)"
输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

示例 4:
输入: "(100)"
输出: [(10, 0)]
解释: 
1.0 是不被允许的。
 
提示:
4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。

"""

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:


        # 方法一：枚举
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n)
        def find(s, count):
            m = len(s)
            res = []
            if str(int(s)) == s:
                res.append(s)
            if count == 0:
                for j in range(1, m):
                    res.append(s[:j] + '.' + s[j:])
            elif count == m:
                return res
            elif s[0] == '0':
                if s[-1] != '0':
                    res.append('0.' + s[1:])
                else:
                    return res
            elif s[-1] == '0':
                return res
            else:
                for j in range(1, m):
                    res.append(s[:j] + '.' + s[j:])
            return res

        s = s[1: -1]
        n = len(s)
        count0 = [0] * (n + 1)
        for i in range(n):
            count0[i + 1] = 1 if s[i] == '0' else 0
            count0[i + 1] += count0[i]
        #print(count0)

        ans = []
        for i in range(1, n):
            s_left = s[: i]
            s_right = s[i:]
            #print(s_left, s_right)
            count_left = count0[i]
            count_right = count0[-1] - count_left
            #print(count_left, count_right)

            left_candi = find(s_left, count_left)
            right_candi = find(s_right, count_right)
            #print('left_candi:', left_candi)
            #print('right_candi:', right_candi)
            for left, right in product(left_candi, right_candi):
                ans.append('(' + left + ', ' + right + ')')
        return ans
            



