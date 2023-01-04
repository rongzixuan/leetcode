"""
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化

返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

示例 1：
输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。

示例 2：
输入：n = 6, index = 1,  maxSum = 10
输出：3
 
提示：
1 <= n <= maxSum <= 10^9
0 <= index < n

"""

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:


        # 方法一：二分 + 贪心（超时）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        def getSum(mid):
            res = mid
            tmp = mid
            for i in range(index - 1, -1, -1):
                tmp = max(tmp - 1, 1)
                res += tmp
            tmp = mid
            for i in range(index + 1, n):
                tmp = max(tmp - 1, 1)
                res += tmp
            return res

        left, right = 1, maxSum
        while left < right:          
            mid = (left + right + 1) // 2
            #print("left, mid, right:", left, mid, right)
            res = getSum(mid)
            #print('res:', res)
            if res > maxSum:
                right = mid - 1
            elif res == maxSum:
                return mid
            elif res < maxSum:
                left = mid
        return right


        # 方法二：二分 + 贪心
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        def getSum(mid):
            res = mid
            left_num = max(1, mid - index)
            left_length = min(index, mid - 1)
            res += (mid - 1 + left_num) * left_length // 2
            #print('left_num, left_length:', left_num, left_length)
            #print('res1:', res)
            if left_length < index:
                res += (index - left_length)
            #print('res2:', res)

            right_num = max(1, mid - n + index + 1)
            right_length = min(n - index - 1, mid - 1)
            res += (mid - 1 + right_num) * right_length // 2
            #print('right_num, right_length:', right_num, right_length)
            #print('res3:', res)
            if right_length < n - index - 1:
                res += (n - 1 - index - right_length)
            #print('res4:', res)
            return res

        left, right = 1, maxSum
        while left < right:          
            mid = (left + right + 1) // 2
            #print("left, mid, right:", left, mid, right)
            res = getSum(mid)
            #print('res:', res)
            if res > maxSum:
                right = mid - 1
            elif res == maxSum:
                return mid
            elif res < maxSum:
                left = mid
        return right






