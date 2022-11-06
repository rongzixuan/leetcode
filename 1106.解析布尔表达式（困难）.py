"""
给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。

有效的表达式需遵循以下约定：
"t"，运算结果为 True
"f"，运算结果为 False
"!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
"&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
"|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
 
示例 1：
输入：expression = "!(f)"
输出：true

示例 2：
输入：expression = "|(f,t)"
输出：true

示例 3：
输入：expression = "&(t,f)"
输出：false

示例 4：
输入：expression = "|(&(t,f,t),!(t))"
输出：false

提示：
1 <= expression.length <= 20000
expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
expression 是以上述形式给出的有效表达式，表示一个布尔值。

"""

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:


        # 方法一：栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        #trans = {"|": |, "!": !, '&': &, 't': True, 'f': False}
        def cal(x, y, op):
            a = True if x == 't' else False
            b = True if y == 't' else False
            ans = a & b if op == '&' else a | b
            return 't' if ans == True else 'f'

        n = len(expression)
        stack_ops = []
        stack_nums = []
        for i, ch in enumerate(expression):
            #print(i, ch)
            if ch == ')':
                op = stack_ops.pop()
                res = stack_nums.pop()
                while stack_nums and stack_nums[-1] != '(':
                    res1 = stack_nums.pop()
                    res = cal(res, res1, op)
                    #print('res1, res:', res1, res)
                    #print(stack_nums)
                if op == '!':
                    res = 'f' if res == 't' else 't'
                stack_nums.pop()
                stack_nums.append(res)          
            elif ch == "(":
                stack_nums.append(ch)
            elif ch == ',':
                continue
            elif ch == '!' or ch == '&' or ch == '|':
                stack_ops.append(ch)
            else:
                stack_nums.append(ch)
        return stack_nums[-1] == 't'


        # 方法二：栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        stk = []
        for c in expression:
            if c in 'tf!&|':
                stk.append(c)
            elif c == ')':
                t = f = 0
                while stk[-1] in 'tf':
                    t += stk[-1] == 't'
                    f += stk[-1] == 'f'
                    stk.pop()
                match stk.pop():
                    case '!':
                        c = 't' if f else 'f'
                    case '&':
                        c = 'f' if f else 't'
                    case '|':
                        c = 't' if t else 'f'
                stk.append(c)
        return stk[0] == 't'

