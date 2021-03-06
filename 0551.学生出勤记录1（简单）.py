"""
给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
按 总出勤 计，学生缺勤（'A'）严格 少于两天。
学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。

如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

"""

class Solution:
    def checkRecord(self, s: str) -> bool:


        # 方法一：自带函数
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        return s.count('A') <= 1 and 'LLL' not in s


        # 方法二：一次遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(s)
        if n < 2:
            return True

        count_A = 0
        count_L = 0
        for i in range(n):
            if s[i] == 'A':
                count_A += 1
                count_L = 0
                if count_A >= 2:
                    return False
            elif s[i] == 'L':
                #print(count_L)
                count_L += 1
                if count_L >= 3:
                    return False
            else:
                count_L = 0

        return True



    
