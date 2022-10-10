"""
给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：
删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。

请你返回纸上能写出的字典序最小的字符串。 

示例 1：
输入：s = "zza"
输出："azz"
解释：用 p 表示写出来的字符串。
一开始，p="" ，s="zza" ，t="" 。
执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。

示例 2：
输入：s = "bac"
输出："abc"
解释：用 p 表示写出来的字符串。
执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。
执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。
执行第一个操作，得到 p="ab" ，s="" ，t="c" 。
执行第二个操作，得到 p="abc" ，s="" ，t="" 。

示例 3：
输入：s = "bdda"
输出："addb"
解释：用 p 表示写出来的字符串。
一开始，p="" ，s="bdda" ，t="" 。
执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。
执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。

提示：
1 <= s.length <= 10^5
s 只包含小写英文字母。

"""

class Solution:
    def robotWithString(self, s: str) -> str:


        # 方法一：贪心（超时）
        # 时间复杂度：
        # 空间复杂度：
        n = len(s)
        ans = ""
        pre_min_ch = ['z'] * n
        aft_min_ch = ['z'] * n
            
        def find(left, right):  
            min_ch = 123  # ascii码
            res = left
            for i in range(left, right + 1):
                ch = s[i]
                if ord(ch) < min_ch:
                    min_ch = ord(ch)
                    res = i
            return res
        
        left, right = 0, n - 1
        while left <= right:
            index = find(left, right)
            #ans += s[left: index + 1][::-1]
            for i in range(left, index + 1):
                pre_min_ch[i] = s[index]
            left = index + 1
        #print(pre_min_ch)
        
        min2 = 'z'
        for i in range(n - 1, -1, -1):
            if s[i] < min2:
                min2 = s[i]
            aft_min_ch[i] = min2
        #print(aft_min_ch)
    
        stack = []
        for i, ch in enumerate(s):
            #print(min_ch[i])
            if len(stack) == 0 or ord(ch) >= ord(stack[-1]) or ord(pre_min_ch[i]) <= ord(ch):
                stack.append(ch)
            while stack and i + 1 < n and ord(stack[-1]) <= ord(pre_min_ch[i + 1]):
                ans += stack.pop()
            #print(i, ch, stack)
        while stack:
            ans += stack.pop()
        return ans


        # 方法二：贪心 + 栈
        # 时间复杂度：O(n + 26)
        # 空间复杂度：O(26 + n)
        ans = []
        cnt = Counter(s)
        min = 0  # 剩余最小字母
        st = []
        for c in s:
            cnt[c] -= 1
            while min < 25 and cnt[ascii_lowercase[min]] == 0:
                min += 1
            st.append(c)
            while st and st[-1] <= ascii_lowercase[min]:
                ans.append(st.pop())
        return ''.join(ans)
        
        
        
