"""
给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

示例 1：
输入：arr = [3,1,3,6]
输出：false

示例 2：
输入：arr = [2,1,2,6]
输出：false

示例 3：
输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
 
提示：
0 <= arr.length <= 3 * 10^4
arr.length 是偶数
-10^5 <= arr[i] <= 10^5

"""

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:


        # 方法一：哈希表 + 排序
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(arr)

        from collections import Counter
        count = Counter(arr)

        for num in sorted(count, key=abs):
            #print(num, count[num])
            if count[2 * num] < count[num]:
                return False
            count[2 * num] -= count[num]

        return True


