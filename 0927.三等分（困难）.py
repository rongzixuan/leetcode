"""
给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
arr[0], arr[1], ..., arr[i] 为第一部分；
arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
这三个部分所表示的二进制值相等。

如果无法做到，就返回 [-1, -1]。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

示例 1：
输入：arr = [1,0,1,0,1]
输出：[0,3]

示例 2：
输入：arr = [1,1,0,1,1]
输出：[-1,-1]

示例 3:
输入：arr = [1,1,0,0,1]
输出：[0,2]
 
提示：
3 <= arr.length <= 3 * 10^4
arr[i] 是 0 或 1

"""

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        count1 = sum([1 for a in arr if a == 1])
        #print(count1)
        if count1 == 0:
            return [0, 2]
        if count1 % 3 != 0:   # 不能等分
            return [-1, -1]
        
        n = len(arr)
        target = count1 // 3
        #print(target)
        count = 0
        i1, i2 = 0, 0  # 第一部分第一次出现0，最后一个出现0
        j1, j2 = 0, 0
        k1, k2 = 0, 0
        for i, a in enumerate(arr):
            if a == 1:
                count += 1   
                if count == 1:
                    i1 = i
                if count == target:
                    i2 = i
                elif (count - 1) == target:
                    j1 = i
                if count == (2 * target):
                    j2 = i
                elif (count - 1) == 2 * target:
                    k1 = i
                if count == count1:
                    k2 = i
            #print(i, count)
        #print(i1, i2, j1, j2, k1, k2)

        remain = n - 1 - k2   # 最后一个数字尾部的0个数
        i = i2 + 1 + remain
        j = j2 + 1 + remain
        part1 = arr[i1: i]
        part2 = arr[j1: j]
        part3 = arr[k1: ]
        #print(part1, part2, part3)
        if part1 != part2 or part1 != part2 or part2 != part3:
            return [-1, -1]
        return [i - 1, j]



