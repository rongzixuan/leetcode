"""
对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。
给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。

示例 1：
输入：s1 = "ab", s2 = "ba"
输出：1

示例 2：
输入：s1 = "abc", s2 = "bca"
输出：2
 
提示：
1 <= s1.length <= 20
s2.length == s1.length
s1 和 s2  只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母
s2 是 s1 的一个字母异位词

"""

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:


        # 方法一：记忆化搜索(回溯)（超时）
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n)
        ans = inf
        #return ans
        n = len(s1)
        used = set()
        #time = 0

        @cache
        def dfs(s, time):        
            nonlocal ans, n
            #print('s, time:', s, time)
            if s == s2:
                #print('s, s2:', s, s2)
                ans = min(ans, time)
                return
            for i in range(n - 1):
                if s[i] == s2[i]:
                    continue
                for j in range(i + 1, n):
                    if s[j] == s2[j]:
                        continue
                    if s[i] != s[j] and(i, j) not in used:
                        #print('i, j:', i, j)
                        tmp = list(s)
                        tmp[i], tmp[j] = tmp[j], tmp[i]
                        s3 = "".join(tmp)
                        used.add((i, j))
                        #time += 1
                        res = dfs(s3, time + 1)
                        used.remove((i, j))
                        #time -= 1
            
        dfs(s1, 0)
        return ans


        # 方法二：记忆化搜索(回溯)
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        ans = inf
        #return ans
        n = len(s1)
        used = set()
        time = 0

        @cache
        def dfs(s1, s2):        
            nonlocal ans, n, time
            #print('s1,, s2, time:', s1, s2, time)
            if not s1 or s1 == s2:
                #print('s, s2:', s, s2)
                #ans = min(ans, time)
                return 0
            candidates1 = [i for i in range(len(s1)) if s1[i] != s2[i]]
            candidates2 = [i for i, index in enumerate(candidates1) if s2[index] == s1[candidates1[0]]]
            s3 = "".join([s1[i] for i in candidates1[1:]])
            ans = inf
            for i, index in enumerate(candidates2):
                candidates1[0], candidates1[index] = candidates1[index], candidates1[0]
                s4 = "".join([s2[i] for i in candidates1[1:]])
                time += 1
                ans = min(ans, dfs(s3, s4))
                time -= 1
                candidates1[0], candidates1[index] = candidates1[index], candidates1[0]
            return ans + 1
            
        return dfs(s1, s2)


        # 方法三：广度优先搜索
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))
            step += 1


        # 方法四：深度优先搜索
        s, t = [], []
        for x, y in zip(s1, s2):
            if x != y:
                s.append(x)
                t.append(y)
        n = len(s)
        if n == 0:
            return 0

        ans = n - 1
        def dfs(i: int, cost: int) -> None:
            nonlocal ans
            if cost > ans:
                return
            while i < n and s[i] == t[i]:
                i += 1
            if i == n:
                ans = min(ans, cost)
                return
            diff = sum(s[j] != t[j] for j in range(i, len(s)))
            min_swap = (diff + 1) // 2
            if cost + min_swap >= ans:  # 当前状态的交换次数下限大于等于当前的最小交换次数
                return
            for j in range(i + 1, n):
                if s[j] == t[i]:
                    s[i], s[j] = s[j], s[i]
                    dfs(i + 1, cost + 1)
                    s[i], s[j] = s[j], s[i]
        dfs(0, 0)
        return ans


