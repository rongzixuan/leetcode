"""
给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。

"""

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        # 方法一：暴力
        a = [False] * 51

        n = len(ranges)
        for i in range(n):
            l, r = ranges[i][0], ranges[i][1]
            for j in range(l, r+1):
                a[j] = True

        for i in range(left, right+1):
            if a[i] == False:
                return False
        return True


        # 方法二：合并区间并标记
        ranges.sort(key = lambda d:d[0])
        #print(ranges)

        a = [False] * 51
        for start, end in ranges:
            l = max(left, start)
            r = min(right, end)
            for i in range(l, r+1):
                a[i] = True

        for i in range(left, right+1):
            if a[i] == False:
                return False
        return True
    

        # 方法三：差分数组 + 前缀和
        diff = [0] * 52
        pre_sum = [0] * 52

        for start, end in ranges:
            diff[start] += 1
            diff[end+1] -= 1
        #print(diff)

        for i in range(1, 52):
            pre_sum[i] = pre_sum[i-1] + diff[i]
        #print(pre_sum)

        for i in range(left, right+1):
            if pre_sum[i] <= 0:
                return False
        
        return True
        


        
        
