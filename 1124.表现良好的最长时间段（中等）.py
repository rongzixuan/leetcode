"""
给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。

我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。

所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。

请你返回「表现良好时间段」的最大长度。

示例 1：
输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。

示例 2：
输入：hours = [6,6,6]
输出：0
 
提示：
1 <= hours.length <= 10^4
0 <= hours[i] <= 16

"""

class Solution:
    def longestWPI(self, hours: List[int]) -> int:


        # 方法一：前缀和（超时）
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(hours)
        pre = [0]
        count1, count0 = 0, 0
        for hour in hours:
            if hour > 8:
                count1 += 1
            else:
                count0 += 1
            pre.append(count1- count0)
        #print(pre)

        ans = 0

        for i in range(1, n + 1):
            for j in range(0, i):
                if pre[i] - pre[j] > 0:
                    ans = max(ans, i - j)
        return ans


        # 方法二：前缀和 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        ans = s = 0
        pos = {}
        for i, x in enumerate(hours):
            s += 1 if x > 8 else -1
            if s > 0:
                ans = i + 1
            elif s - 1 in pos:
                ans = max(ans, i - pos[s - 1])
            if s not in pos:
                pos[s] = i
        return ans


        # 方法三：前缀和 + 单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(hours)
        pre = [0] * (n + 1)  # 前缀和
        stack = [0]  # pre[0]
        for j, h in enumerate(hours, 1):
            pre[j] = pre[j - 1] + (1 if h > 8 else -1)
            if pre[j] < pre[stack[-1]]: stack.append(j)  # 感兴趣的 j
        #print('pre:', pre)
        #print('stack:', stack)

        ans = 0
        for i in range(n, 0, -1):
            while stack and pre[i] > pre[stack[-1]]:
                ans = max(ans, i - stack.pop())  # [st[-1],i) 可能是最长子数组
        return ans




