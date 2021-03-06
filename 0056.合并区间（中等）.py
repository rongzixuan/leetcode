"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 方法一：排序
        n = len(intervals)
        if n == 0:
            return []

        intervals.sort(key = lambda d:d[0])    
        #print(intervals)      
        res = []
        pre_left, pre_right = intervals[0][0], intervals[0][1] 
             
        for i in range(1, n):
            interval = intervals[i]
            left, right = interval[0], interval[1]        
            #print(left, right)
            if right < pre_right:
                #print('1')
                #pre_right = right  
                continue  
            elif right >= pre_right and left <= pre_right:
                #print('2')
                pre_right = right 
            else:
                #print('3')
                res.append([pre_left, pre_right])
                pre_left = left 
                pre_right = right 
                
        res.append([pre_left, pre_right])

        return res


        # 方法二：排序2
        res = []
        intervals.sort(key = lambda d:d[0])

        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append([interval[0], interval[1]])
            else:
                res[-1][1] = max(interval[1], res[-1][1])

        return res



    
