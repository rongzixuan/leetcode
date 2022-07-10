"""
给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。

你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。

示例 1：
输入：n = 13
输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]

示例 2：
输入：n = 2
输出：[1,2]
 
提示：
1 <= n <= 5 * 10^4

"""


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:


        # 方法一：深度优先搜索（递归）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        ans = []

        def dfs(num):
            for i in range(0, 10):
                #print(num, i)
                new_num = num * 10 + i
                if new_num <= n:
                    ans.append(new_num)
                    dfs(new_num)

        for i in range(1, 10):
            if i <= n:
                ans.append(i)
                dfs(i)

        return ans


        # 方法二：深度优先搜索（栈）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        ans = [0] * n

        num = 1
        for i in range(n):
            ans[i] = num            
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or (num + 1) > n:
                    num //= 10 
                num += 1

        return ans


