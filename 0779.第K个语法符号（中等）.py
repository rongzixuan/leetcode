"""
我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。

给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）

示例 1:
输入: n = 1, k = 1
输出: 0
解释: 第一行：0

示例 2:
输入: n = 2, k = 1
输出: 0
解释: 
第一行: 0 
第二行: 01

示例 3:
输入: n = 2, k = 2
输出: 1
解释:
第一行: 0
第二行: 01

提示:
1 <= n <= 30
1 <= k <= 2^n - 1

"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:


        # 方法一：递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 1:
            return 0
        res = self.kthGrammar(n - 1, (k + 1) // 2)
        return 1 if ((res == 1 and k % 2 == 1) or (res == 0 and k % 2 == 0)) else 0


        # 方法二：找规律 + 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 1:
            return 0
        if k <= 2**(n - 1) // 2:
            return self.kthGrammar(n - 1, k)
        return 1 - self.kthGrammar(n - 1, k - 2**(n - 1) // 2)


        # 方法三：找规律 + 位运算
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        return (k - 1).bit_count() % 2

        
