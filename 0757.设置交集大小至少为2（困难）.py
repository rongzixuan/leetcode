"""
一个整数区间 [a, b]  ( a < b ) 代表着从 a 到 b 的所有连续整数，包括 a 和 b。
给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。
输出这个最小集合S的大小。

示例 1:
输入: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
输出: 3
解释:
考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
且这是S最小的情况，故我们输出3。

示例 2:
输入: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
输出: 5
解释:
最小的集合S = {1, 2, 3, 4, 5}.

注意:
intervals 的长度范围为[1, 3000]。
intervals[i] 长度为 2，分别代表左、右边界。
intervals[i][j] 的值是 [0, 10^8]范围内的整数。

"""

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:


        # 方法一：贪心
        # 时间复杂度：
        # 空间复杂度：
        intervals.sort(key=lambda x: (x[1], -x[0]))

        """li = [-1,-1]
        for x in intervals:
            print('x[0], x[1]:', x[0], x[1])
            if x[0] <= li[-2]:
                continue
            if x[0] > li[-1]:
                li.append(x[1]-1)
            li.append(x[1])
            print('li:', li)
        return len(li) - 2"""

        ans = []
        for left, right in intervals:
            #print('left, right:', left, right)
            if len(ans) == 0:
                ans.append(right - 1)
                ans.append(right)
            else:
                if left <= ans[-2]:
                    continue
                elif left > ans[-1]:
                    ans.append(right - 1)
                ans.append(right)
            #print('ans:', ans)

        return len(ans)


