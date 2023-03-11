"""
给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

示例 1:
输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]

示例 2:
输入: ["A","A"]
输出: []

提示：
array.length <= 100000

"""

class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]: 


        # 方法一：前缀和 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(array)
        count = {0: 0}
        pre = [0]
        tmp = 0
        max_length = 0
        ans = -1
        for i in range(1, n + 1):
            if array[i - 1][0].isalpha():
                tmp += 1
            else:
                tmp -= 1
            if tmp in count:
                if i - count[tmp] > max_length:
                    max_length = i - count[tmp]
                    ans = count[tmp]
            else:
                count[tmp] = i
        return array[ans: ans + max_length]

        



