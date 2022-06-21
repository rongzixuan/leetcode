"""
给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

"""


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:


        # 方法一：回溯
        # 时间复杂度：O(4 ** n)
        # 空间复杂度：O(n)
        n = len(num)     
        if n == 1:
            if num != str(target):
                return []
            else:
                return [num]

        ans = []
        def backtrack(depth, expr, res, mul):
            if depth == n:
                if res == target:
                    ans.append("".join(expr))
                return 

            length = len(expr)
            if depth:
                expr.append("")

            for j in range(depth, n):  # depth后面可以取的数字长度
                if j > depth and num[depth] == '0':
                    break
                tmp_num = int(num[depth: j+1])
                expr.append(num[j])
                #print(expr)
                if depth == 0:                   
                    backtrack(j + 1, expr, tmp_num, tmp_num)
                else:
                    expr[length] = "+"
                    backtrack(j + 1, expr, res + tmp_num, tmp_num)

                    expr[length] = "-"
                    backtrack(j + 1, expr, res - tmp_num, -tmp_num)

                    expr[length] = "*"
                    backtrack(j + 1, expr, res - mul + mul * tmp_num, mul * tmp_num)
            del expr[length: ]

        backtrack(0, [], 0, 0)
        return ans


