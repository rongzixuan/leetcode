"""
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        # 方法一：递归
        # 时间复杂度：O(2^n * n)
        # 空间复杂度：O(2^n * n)
        n = len(s)
        ans = [[]]

        for i in range(n):
            m = len(ans)

            if s[i].isdigit():
                for j in range(m):
                    ans[j].append(s[i])
            elif s[i].isalpha():
                for j in range(m):
                    ans.append(ans[j][:])
                    ans[j].append(s[i].lower())
                    ans[j+m].append(s[i].upper())

        return ["".join(x) for x in ans]
        
        
        # 方法二：内置库函数
        # 时间复杂度：O(2^n * n)
        # 空间复杂度：O(2^n * n)
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, s)))
        

        # 方法一：回溯
        # 时间复杂度：O(n * 2**n)
        # 空间复杂度：O(n * 2**n)
        n = len(s)
        ans = []

        def dfs(index, tmp_s):
            if index == n:
                ans.append(tmp_s)
            else:
                ch1 = s[index]
                if ch1.isalpha():
                    ch2 = chr(ord(ch1) + 32) if ord(ch1) < 97 else chr(ord(ch1) - 32)
                    dfs(index + 1, tmp_s + ch1)
                    dfs(index + 1, tmp_s + ch2)
                else:
                    dfs(index + 1, tmp_s + ch1)

        dfs(0, "")
        return ans


        # 方法二：广度优先搜索
        # 时间复杂度：O(n * 2**n)
        # 空间复杂度：O(n * 2**n)
        ans = []
        q = deque([''])
        while q:
            cur = q[0]
            pos = len(cur)
            if pos == len(s):
                ans.append(cur)
                q.popleft()
            else:
                if s[pos].isalpha():
                    q.append(cur + s[pos].swapcase())
                q[0] += s[pos]
        return ans


        # 方法三：二进制位图
        # 时间复杂度：O(n * 2**n)
        # 空间复杂度：O(1)
        ans = []
        m = sum(c.isalpha() for c in s)
        for mask in range(1 << m):
            t, k = [], 0
            for c in s:
                if c.isalpha():
                    t.append(c.upper() if mask >> k & 1 else c.lower())
                    k += 1
                else:
                    t.append(c)
            ans.append(''.join(t))
        return ans





