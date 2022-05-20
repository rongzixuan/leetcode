"""
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。
返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

示例 1：
输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。\

示例 2：
输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。

示例 3：
输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
 
提示：
1 <= intervals.length <= 2 * 10^4
intervals[i].length == 2
-10^6 <= starti <= endi <= 10^6
每个间隔的起点都 不相同

"""


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:


        # 方法一：二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        def getBigger(num, index):
            n = len(index)
            left, right = 0, n - 1
            while left < right:
                mid = left + (right - left) // 2
                if index[mid] < num:
                    left = mid + 1
                elif index[mid] > num:
                    right = mid
                else:
                    #print('mid:', mid)
                    return mid
            #print('left, right:', left, right)
            return left if index[left] >= num else -1

        n = len(intervals)
        if n == 1:
            return [-1]
        
        index = []
        index_dict = {}
        for i in range(n):
            index.append(intervals[i][0])
            index_dict[intervals[i][0]] = i
        index.sort()
        #print(index)

        res = []
        for i in range(n):
            #print('i:', i)
            tmp_res = i
            if intervals[i][0] != intervals[i][1]:
                right = getBigger(intervals[i][1], index)
                tmp_res = index_dict[index[right]] if right != -1 else -1
            res.append(tmp_res) 
        return res


        # 方法二：双指针
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(intervals)
        starts, ends = list(zip(*intervals))
        #print(starts)
        #print(ends)
        starts = sorted(zip(starts, range(n)))
        ends = sorted(zip(ends, range(n)))
        #print(starts)
        #print(ends)

        ans, j = [-1] * n, 0
        for end, id in ends:
            while j < n and starts[j][0] < end:
                j += 1
            if j < n:
                ans[id] = starts[j][1]
        return ans





