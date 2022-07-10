"""
给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。
列表中的每个元素只可能是整数或整数嵌套列表

示例 1：
输入：s = "324",
输出：324
解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。

示例 2：
输入：s = "[123,[456,[789]]]",
输出：[123,[456,[789]]]
解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789
 
提示：
1 <= s.length <= 5 * 10^4
s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成
用例保证 s 是可解析的 NestedInteger
输入中的所有值的范围是 [-10^6, 10^6]

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        index= 0

        def dfs():
            nonlocal index
            if s[index] == '[':
                ni = NestedInteger()
                index += 1
                while s[index] != ']':
                    ni.add(dfs())
                    if s[index] == ',':
                        index += 1
                index += 1
                return ni
            else:
                nagative = True if s[index] == '-' else False   # 是否是负数
                if nagative:
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num *= 10
                    num += int(s[index])
                    index += 1
                if nagative:
                    num = -num
                return NestedInteger(num) 

        return dfs()


        # 方法二：栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        nagative = False
        num = 0
        for index, ch in enumerate(s):
            if ch == '[':
                stack.append(NestedInteger())
            elif ch in ',]':
                if s[index - 1].isdigit():
                    if nagative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num, nagative = 0, False
                if ch == ']' and len(stack) > 1:
                    stack[-2].add(stack.pop())
            elif ch == '-':
                nagative = True
            elif ch.isdigit():
                num = num * 10 + int(ch)

        return stack.pop()


    
    
