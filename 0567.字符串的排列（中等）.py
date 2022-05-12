"""
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        # 方法一：双指针（超时）
        # 时间复杂度：O(n * m)
        # 空间复杂度：O(m)
        m, n = len(s1), len(s2)
        from collections import defaultdict
        hash_table = defaultdict(int)

        for i in range(m):
            hash_table[s1[i]] += 1
        #print(hash_table)

        j = 0
        for i in range(n):
            if s2[i] not in hash_table:
                #print('i:', i)
                j = i
                continue
            else:
                #print('i:', i)
                #print('hash_table before:', hash_table)
                j = i
                while j < n and (j - i) < (m) and s2[j] in hash_table:
                    hash_table[s2[j]] -= 1
                    j += 1

                flag = True
                #print('hash_table after:', hash_table)
                for k, v in hash_table.items():
                    if v != 0:
                        flag = False

                if flag:
                    return True 
                else:
                    for k in range(i, j):
                        hash_table[s2[k]] += 1

        return False


        # 方法二：滑动窗口1
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        m, n = len(s1), len(s2)
        if m > n:
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(m):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(m, n):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i-m]) - ord('a')] -= 1
            if count1 == count2:
                return True

        return False


        # 方法三：滑动窗口2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        m, n = len(s1), len(s2)
        if m > n:
            return False
       
        count = [0] * 26
        for i in range(m):
            count[ord(s1[i]) - ord('a')] -= 1
            count[ord(s2[i]) - ord('a')] += 1
        
        diff = 0
        for ch in count:
            if ch != 0:
                diff += 1
        if diff == 0:
            return True

        for i in range(m, n):
            x, y = ord(s2[i]) - ord('a'), ord(s2[i-m]) - ord('a')
            if x == y:
                continue

            if count[x] == 0:
                diff += 1
            count[x] += 1
            if count[x] == 0:
                diff -= 1

            if count[y] == 0:
                diff += 1
            count[y] -= 1
            if count[y] == 0:
                diff -= 1

            if diff == 0:
                return True

        return False


        # 方法四：双指针
        # 时间复杂度：O(n+m)
        # 空间复杂度：O(1)
        m, n = len(s1), len(s2)
        from collections import defaultdict
        hash_table = defaultdict(int)

        for i in range(m):
            hash_table[s1[i]] -= 1
        #print(hash_table)

        j = 0
        for i in range(n):
            #print('i, j:', i, j)
            #print('hash_table before:', hash_table)
            hash_table[s2[i]] += 1

            while hash_table[s2[i]] > 0:
                #print(j)
                hash_table[s2[j]] -= 1
                j += 1
            #print('hash_table after:', hash_table)

            if i - j + 1 == m:
                return True

        return False
