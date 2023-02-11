"""
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：day、month 和 year，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

示例 1：
输入：day = 31, month = 8, year = 2019
输出："Saturday"

示例 2：
输入：day = 18, month = 7, year = 1999
输出："Sunday"

示例 3：
输入：day = 15, month = 8, year = 1993
输出："Sunday"
 
提示：
给出的日期一定是在 1971 到 2100 年之间的有效日期。

"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:


        # 方法一：模拟
        # 时间复杂度：O(C)
        # 空间复杂度：O(1)
        weeks = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        bench = '1970-01-01'

        cnt = 0
        # 统计年
        for i in range(1971, year):
            #print(i)
            if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
                cnt += 366
            else:
                cnt += 365

        # 统计月
        for i in range(1, month):
            #print(i, month_days[i - 1])
            cnt += month_days[i - 1]

        # 统计日
        cnt += day
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month > 2:
            cnt += 1

        return weeks[cnt % 7]



    
    
