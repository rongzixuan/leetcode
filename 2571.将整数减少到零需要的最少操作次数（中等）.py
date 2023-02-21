"""
给你一个正整数 n ，你可以执行下述操作 任意 次：
n 加上或减去 2 的某个 幂

返回使 n 等于 0 需要执行的 最少 操作数。

如果 x == 2i 且其中 i >= 0 ，则数字 x 是 2 的幂。

示例 1：
输入：n = 39
输出：3
解释：我们可以执行下述操作：
- n 加上 20 = 1 ，得到 n = 40 。
- n 减去 23 = 8 ，得到 n = 32 。
- n 减去 25 = 32 ，得到 n = 0 。
可以证明使 n 等于 0 需要执行的最少操作数是 3 。

示例 2：
输入：n = 54
输出：3
解释：我们可以执行下述操作：
- n 加上 21 = 2 ，得到 n = 56 。
- n 加上 23 = 8 ，得到 n = 64 。
- n 减去 26 = 64 ，得到 n = 0 。
使 n 等于 0 需要执行的最少操作数是 3 。  

提示：
1 <= n <= 10^5

"""

class Solution:
    def minOperations(self, n: int) -> int:
        
             
        # 方法一：记忆化搜索（超时）
        # 时间复杂度：
        # 空间复杂度：
        @cache
        def dfs(target):
            #print(target)
            if target == 0:
                return 0
            if (target & (target - 1)) == 0:  # 是2的幂次
                return 1
            res = inf
            for i in range(0, 20):
                if target + (1<<i) <= 2**17 and target + (1<<i) not in used:
                    used.add(target + (1<<i))
                    res = min(res, dfs(target + (1<<i)) + 1)
                    used.remove(target + (1<<i))

                if target - (1<<i) >= 0 and target - (1<<i) not in used:
                    used.add(target - (1<<i))
                    res = min(res, dfs(target - (1<<i)) + 1)
                    used.remove(target - (1<<i))             
            return res
        
        used = set([n])
        return dfs(n)


        # 方法二：广度优先搜索
        # 时间复杂度：
        # 空间复杂度：
        # 如果是2的幂 为0
        if n == 1:
            return 1
        queue = deque([(n, 0)])
        visited = set([n])
        while queue:
            cur, step = queue.popleft()
            if cur == 0:
                return step
            for i in range(20):
                nxt = cur - (1 << i)
                if nxt >= 0 and nxt not in visited:
                    queue.append((nxt, step + 1))
                    visited.add(nxt)
                nxt = cur + (1 << i)
                if nxt not in visited and nxt <= 1 << 18:
                    queue.append((nxt, step + 1))
                    visited.add(nxt)


        # 方法三：贪心 + 位运算
        # 时间复杂度：(logn)
        # 空间复杂度：O(1)
        """
        把 n 看成二进制数，那么更高位的比特 1 是会受到更低位的比特 1 的加减影响的，但是，最小的比特1 没有这个约束。

那么考虑优先消除最小的比特 1，设它对应的数字为 lowbit。

消除方法只能是加上 lowbit，或者减去 lowbit。

贪心的策略是：如果有多个连续 1，那么采用加法是更优的，可以一次消除多个 1；否则对于单个 1，减法更优。

        """
        ans = 1
        while n & (n - 1):  # 不是 2 的幂次
            lb = n & -n
            if n & (lb << 1): n += lb  # 多个连续 1
            else: n -= lb  # 单个 1
            ans += 1
        return ans


        # 方法四：记忆化搜索
        # 时间复杂度：
        # 空间复杂度：
        @cache
        def dfs(n):
            if (n & (n-1)) == 0:
                return 1
            lowbit = n & (-n)
            return min(dfs(n - lowbit), dfs(n + lowbit)) + 1

        return dfs(n)






