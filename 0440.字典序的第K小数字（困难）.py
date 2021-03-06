"""
给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。

示例 1:
输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

示例 2:
输入: n = 1, k = 1
输出: 1
 
提示:
1 <= k <= n <= 10^9

"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:


        # 方法一：字典树思想 + 深度优先搜索（超时）
        # 时间复杂度：O(k * n)
        # 空间复杂度：O(k)
        i = 0
        from collections import deque
        stack = deque([9, 8, 7, 6, 5, 4, 3, 2, 1])

        while i <= k and stack:
            node = stack.pop()
            i += 1
            #print(node)
            if i == k:
                return node
            for j in range(9, -1, -1):
                if node * 10 + j <= n:
                    stack.append(node * 10 + j)


        # 方法二：字典树思想
        # 时间复杂度：O(logn * logm)
        # 空间复杂度：O(1)       
        def getChildNum(node):  # 统计node所有子结点的个数（包括自己）
            count = 0
            left, right = node, node
            while left <= n:
                count += (min(right, n) - left + 1)
                left *= 10
                right = right * 10 + 9
            #print('node, count:', node, count)

            return count

        node = 1
        k -= 1
        while k:
            child_num = getChildNum(node)
            if child_num > k:
                node *= 10
                k -= 1
            else:
                node += 1
                k -= child_num

        return node



