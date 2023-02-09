"""
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数

"""

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        # 方法一：差分数组
        # 时间复杂度：O(m+n)，其中m为bookings数组长度
        # 空间复杂度：O(n)
        answer = [0] * (n+1)

        for first, last, seat in bookings:
            answer[first-1] += seat
            answer[last] -= seat
        #print(answer)

        for i in range(1, n+1):
            answer[i] += answer[i-1]
        #print(answer)

        return answer[:n]

    
    
    
    
    
