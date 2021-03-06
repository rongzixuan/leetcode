"""
假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
第 i 位的数字能被 i 整除
i 能被第 i 位上的数字整除

现在给定一个整数 N，请问可以构造多少个优美的排列？

"""

class Solution:
    def countArrangement(self, n: int) -> int:


        # 方法一：回溯
        # 时间复杂度：O(n!)
        # 空间复杂度：O(n^2)
        count = 0
        visited = set()
        match = defaultdict(list)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)
        #print(match)

        index = 1        
        def backtrack(n, index):
            if index == n + 1:
                nonlocal count
                count += 1
                return 
            for x in match[index]:
                if x not in visited:
                    visited.add(x)
                    backtrack(n, index+1)
                    visited.discard(x)

        backtrack(n, index)
        return count


        # 方法二：状态压缩 + 动态规划 
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(2^n)
        f = [0] * (1 << n)
        f[0] = 1
        
        for mask in range(1, 1 << n):
            num = bin(mask).count('1')
            for i in range(n):
                if mask & (1 << i) and ((i+1) % num == 0 or num % (i+1) == 0):
                    f[mask] += f[mask ^ (1 << i)]

        #print(f)
        return f[(1 << n) - 1] 


            


