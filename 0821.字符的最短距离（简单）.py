"""
给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。

返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。

两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。

 

示例 1：
输入：s = "loveleetcode", c = "e"
输出：[3,2,1,0,1,0,0,1,2,2,1,0]
解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。

示例 2：
输入：s = "aaab", c = "b"
输出：[3,2,1,0]
 

提示：
1 <= s.length <= 10^4
s[i] 和 c 均为小写英文字母
题目数据保证 c 在 s 中至少出现一次

"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:


        # 方法一：遍历 + 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)

        c_list = []
        for i, ch in enumerate(s):
            if ch == c:
                c_list.append(i)
        #print(c_list)

        j = 0
        res = [float('inf')] * n
        for i, ch in enumerate(s):
            while j < len(c_list) and i > c_list[j]:
                j += 1
            #print(i, j)
            
            if j < len(c_list):
                res[i] = min(res[i], abs(i - c_list[j]))
            if j - 1 >= 0:
                res[i] = min(res[i], abs(i - c_list[j - 1]))
            #print(res[i])

        return 
        

        # 方法二：正反两次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(s)
        res = [float('inf')] * n

        left_index = float('-inf')
        for i, ch in enumerate(s):
            if ch == c:
                left_index = i
            res[i] = min(res[i], abs(i - left_index))


        right_index = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                right_index = i
            res[i] = min(res[i], abs(i - right_index))

        return res





