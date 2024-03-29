"""
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

示例 1：
输入：date = "2019-01-09"
输出：9

示例 2：
输入：date = "2019-02-10"
输出：41

示例 3：
输入：date = "2003-03-01"
输出：60

示例 4：
输入：date = "2004-03-01"
输出：61
 
提示：
date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日

"""


class Solution:
    def dayOfYear(self, date: str) -> int:


        # 方法一：模拟
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = 0

        # 月份
        date_month = int(date[5: 7])
        if date_month > 1:
            for i in range(date_month - 1):
                res += days[i] 

        # 日
        date_day = int(date[8:])
        res += date_day

        # 年
        date_year = int(date[:4])
        if date_year % 400 == 0 or (date_year % 4 == 0 and date_year % 100 != 0):
            if date_month > 2:
                res += 1

        return res

    
    
    
