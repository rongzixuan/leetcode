"""
给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。

给你一个整数 k ，表示想要 连续 黑色块的数目。

每一次操作中，你可以选择一个白色块将它 涂成 黑色块。

请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。

示例 1：
输入：blocks = "WBBWWBBWBW", k = 7
输出：3
解释：
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。

示例 2：
输入：blocks = "WBWBBBW", k = 2
输出：0
解释：
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。
 
提示：
n == blocks.length
1 <= n <= 100
blocks[i] 要么是 'W' ，要么是 'B' 。
1 <= k <= n

"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:


        # 方法一：前缀和
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(blocks)
        pre = list(accumulate([1 if ch == 'B' else 0 for ch in blocks], initial=0))
        #print(pre)

        ans = inf
        for i in range(k, n + 1):
            ans = min(ans, k - pre[i] + pre[i - k])
        return ans


        # 方法二：滑动窗口
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(blocks)
        count = sum([1 if ch == 'B' else 0 for ch in blocks[:k]])
        left = 0
        ans = k - count
        for right in range(k, n):
            if blocks[right] == 'B':
                count += 1
            if blocks[left] == 'B':
                count -= 1
            left += 1
            ans = min(ans, k - count)
        return ans




