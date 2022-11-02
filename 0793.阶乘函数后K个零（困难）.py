"""
f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。
例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。
给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。

示例 1：
输入：k = 0
输出：5
解释：0!, 1!, 2!, 3!, 和 4! 均符合 k = 0 的条件。

示例 2：
输入：k = 5
输出：0
解释：没有匹配到这样的 x!，符合 k = 5 的条件。

示例 3:
输入: k = 3
输出: 5

提示:
0 <= k <= 10^9

"""

class Solution:
    def preimageSizeFZF(self, k: int) -> int:


        # 方法一：二分查找
        # 时间复杂度：O(logk * logk)
        # 空间复杂度：O(1)
        # 10 = 2 * 5
        def judge(num):
            count = 5
            res = 0
            while count <= num:
                res += num // count
                count *= 5
            return res

        left = 0
        right = 5 * k
        while left <= right:
            mid = left + (right - left) // 2
            #print(left, mid, right)
            res = judge(mid)
            if res == k:  # 存在数字mid，使得mid!中包含5的数量为k
                return 5
            elif res < k:
                left = mid + 1
            else:
                right = mid - 1
        return 0



