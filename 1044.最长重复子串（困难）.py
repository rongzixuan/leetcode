"""
给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

返回 任意一个 具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。

示例 1：
输入：s = "banana"
输出："ana"

示例 2：
输入：s = "abcd"
输出：""

提示：
2 <= s.length <= 3 * 10^4
s 由小写英文字母组成

"""

class Solution:
    def longestDupSubstring(self, s: str) -> str:


        # 方法一：哈希表
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(s)

        from collections import defaultdict
        hash_table = defaultdict(list)
        hash_table2 = defaultdict(list)
        #print(hash_table)
        for i in range(n):
            for j in range(i, n):
                if s[i: j+1] in hash_table:
                    #print('i, j:', i, j, hash_table[s[i: j+1]]) 
                    hash_table[s[i: j+1]] = [hash_table[s[i: j+1]][0] + 1, j - i + 1]
                else:
                    #print(False)
                    #print('i, j:', i, j, hash_table[s[i: j+1]])                    
                    hash_table[s[i: j+1]] = [1, j - i + 1]

        #print(hash_table)
        new = sorted(hash_table.items(), key = lambda x: x[1][1], reverse=True)
        #print('new:', new)

        for k, v in new:
            if v[0] > 1:
                return k

        return


        # 方法二：模拟
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        n = len(s)

        ans = ''
        max_len = i = 0  # i代表子串的开始， j代表子串的结束
        j = 1
        while i < len(s):
            #print('i, j before:', i, j)
            #print('s[i: j]:', s[i: j])
            if s[i: j] in s and s[i: j] in s[i + 1:]:  # 判定子串是否2次出现，如果是，则判断是否是最大长度，并增加子串长度
                if max_len < j - i:
                    max_len = j - i
                    ans = s[i: j]
                j += 1
                #i -= 1
            else:
                i += 1
            #print('i, j after:', i, j)
        return ans


        # 方法三：模拟
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        ans = ""
        for i in range(len(s)):
            while s[i:i+len(ans)+1] in s[i+1:]:
                ans = s[i:i+len(ans) + 1]
        return ans


        # 方法四：二分法 + 字符串哈希
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 生成两个进制
        def check(arr, a1, a2, mod1, mod2, mid):
            n = len(arr)
            aL1, aL2 = pow(a1, mid, mod1), pow(a2, mid, mod2)
            h1, h2 = 0, 0
            for i in range(mid):
                h1 = (h1 * a1 + arr[i]) % mod1
                h2 = (h2 * a2 + arr[i]) % mod2
            used = {(h1, h2)}

            for i in range(1, n - mid + 1):
                h1 = (h1 * a1 - arr[i - 1] * aL1 + arr[i + mid - 1]) % mod1
                h2 = (h2 * a2 - arr[i - 1] * aL2 + arr[i + mid - 1]) % mod2
                if (h1, h2) in used:
                    return i
                else:
                    used.add((h1, h2))
            return -1

        a1, a2 = random.randint(26, 100), random.randint(26, 100)  # 生成两个进制
        # 生成两个模
        mod1, mod2 = random.randint(10**9+7, 2**31-1), random.randint(10**9+7, 2**31-1)
        n = len(s)
        arr = [ord(c) - ord('a') for c in s]
        #print('arr:', arr)

        left, right = 0, n-1
        length = 0
        start = -1
        while left <= right:
            mid = left + (right - left) // 2
            idx = check(arr, a1, a2, mod1, mod2, mid)
            if idx != -1:
                left = mid + 1
                length = mid
                start = idx
            else:
                right = mid - 1

        return s[start: start + length] if start != -1 else ""


    

        
   
