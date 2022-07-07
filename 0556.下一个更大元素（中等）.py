"""
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

示例 1：
输入：n = 12
输出：21

示例 2：
输入：n = 21
输出：-1
 
提示：
1 <= n <= 2^31 - 1

"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:


        # 方法一：模拟
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        from sortedcontainers import SortedList
        num = str(n)
        length = len(num)
        if all(int(num[i - 1]) >= int(num[i]) for i in range(1, length)):
            return -1

        used = SortedList()
        index1 = length - 1  # 第一个
        for i in range(length - 1, -1, -1):
            #print(i)
            if used and int(num[i]) < int(used[-1]):
                index1 = i
                break         
            used.add(num[i])

        index2 = length  # 第二个
        for i in range(length - 1, index1, -1):
            if num[i] > num[index1] and (index2 == length or num[i] < num[index2]):
                index2 = i

        #print(index1, index2)
        res =  num[:index1] + num[index2] + num[index1 + 1: index2] + num[index1] + num[index2 + 1:]
        #print('res:', res)
        ans = int(res[:index1 + 1] + "".join(sorted(res[index1 + 1:])))
        return ans if ans < 2 ** 31 else -1


        # 方法二：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        from sortedcontainers import SortedList
        num = str(n)
        length = len(num)
        if all(int(num[i - 1]) >= int(num[i]) for i in range(1, length)):
            return -1

        max_index = length - 1
        index1 = length - 1  # 第一个
        for i in range(length - 1, -1, -1):
            #print(i)
            if int(num[i]) < int(num[max_index]):
                index1 = i
                break 
            elif int(num[i]) > int(num[max_index]):        
                max_index = i

        index2 = length  # 第二个
        for i in range(length - 1, index1, -1):
            if num[i] > num[index1] and (index2 == length or num[i] < num[index2]):
                index2 = i

        #print(index1, index2)
        res =  num[:index1] + num[index2] + num[index1 + 1: index2] + num[index1] + num[index2 + 1:]
        #print('res:', res)
        ans = int(res[:index1 + 1] + "".join(sorted(res[index1 + 1:])))
        return ans if ans < 2 ** 31 else -1


