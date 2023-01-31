"""
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。

请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。

示例 1:
输入：s = "**|**|***|", queries = [[2,5],[5,9]]
输出：[2,3]
解释：
- queries[0] 有两个盘子在蜡烛之间。
- queries[1] 有三个盘子在蜡烛之间。

示例 2:
输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
输出：[9,0,0,0,0]
解释：
- queries[0] 有 9 个盘子在蜡烛之间。
- 另一个查询没有盘子在蜡烛之间。
 
提示：
3 <= s.length <= 10^5
s 只包含字符 '*' 和 '|' 。
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= lefti <= righti < s.length

"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:


        # 方法一：预处理 + 前缀和 + 二分法
        # 时间复杂度：O(n + m * lognC) , m = len(queries), C = len(candle_list)
        # 空间复杂度：O(n)
        n = len(s)
        #print('n:', n)
        left, right, candle = -1, n, 0    # 左边/右边的蜡烛，蜡烛总数
        left_index, right_index = [-1] * n, [n] * n  # 左边/右边距离最近的蜡烛位置
        candle_count = [0] * n       # 蜡烛个数
        candle_list = []             # 蜡烛列表
        for i in range(n):
            if s[i] == '|':
                left = i
                candle += 1
                candle_list.append(i)
            left_index[i] = left
            candle_count[i] = candle

            if s[n - 1 - i] == '|':
                right = n - 1 - i
            right_index[n - 1 - i] = right
        #print('left_index:', left_index)
        #print('right_index:', right_index) 
        #print('candle_count:', candle_count)
        #print('candle_list:', candle_list)

        ans = []
        for i, (start, end) in enumerate(queries):
            #print('i, start, end:', i, start, end)
            # 方法三：二分法
            low, high = 0, len(candle_list) - 1
            while low <= high:               
                mid = low + (high - low) // 2
                #print('low, mid, high1:', low, mid, high)
                if candle_list[mid] == start:
                    low = mid
                    break
                elif candle_list[mid] < start:
                    low = mid + 1
                else:
                    high = mid - 1
            if low >= len(candle_list) or low < 0:
                ans.append(0)
                continue
            left = candle_list[low]
            while left < n and s[left] == '|':
                left += 1           
            #print('left:', left)

            low, high = 0, len(candle_list) - 1
            while low <= high:               
                mid = low + (high - low) // 2
                #print('low, mid, high1:', low, mid, high)
                if candle_list[mid] == end:
                    high = mid
                    break
                elif candle_list[mid] < end:
                    low = mid + 1
                else:
                    high = mid - 1
            if high < 0 or high > len(candle_list):
                ans.append(0)
                continue
            right = candle_list[high]
            while 0 <= right and s[right] == '|':
                right -= 1          
            #print('left, right:', left, right)
            
            if right >= left:
                count = right - left + 1 - (candle_count[right] - candle_count[left]) 
            else:
                count = 0
            ans.append(count)

        return ans


        # 方法二：预处理 + 前缀和
        # 时间复杂度：O(n + m) , m = len(queries), C = len(candle_list)
        # 空间复杂度：O(n)
        n = len(s)
        #print('n:', n)
        left, right, candle = -1, n, 0    # 左边/右边的蜡烛，蜡烛总数
        left_index, right_index = [-1] * n, [n] * n  # 左边/右边距离最近的蜡烛位置
        candle_count = [0] * n       # 蜡烛个数
        for i in range(n):
            if s[i] == '|':
                left = i
                candle += 1
            left_index[i] = left
            candle_count[i] = candle

            if s[n - 1 - i] == '|':
                right = n - 1 - i
            right_index[n - 1 - i] = right


        ans = []
        for i, (start, end) in enumerate(queries):
            x, y = right_index[start], left_index[end]
            if y > x:
                #print(i)
                ans.append(y - x - candle_count[y] + candle_count[x])
            else:
                ans.append(0)

        return ans



        
