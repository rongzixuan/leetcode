"""
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
由于答案可能很大，因此 返回答案模 10^9 + 7 。

示例 1：
输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

示例 2：
输入：arr = [11,81,94,43,3]
输出：444

提示：
1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4

"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:


        # 方法一：单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(arr)
        
        stack1 = []
        left_min = [-1] * n
        for i in range(n):
            while stack1 and stack1[-1][1] >= arr[i]:
                stack1.pop()  
            if len(stack1) > 0:
                left_min[i] = stack1[-1][0]
            stack1.append((i, arr[i]))
        #print(left_min)

        stack2 = []
        right_min = [n] * n
        for i in range(n - 1, -1, -1):
            while stack2 and stack2[-1][1] > arr[i]:
                stack2.pop()  
            if len(stack2) > 0:
                right_min[i] = stack2[-1][0]
            stack2.append((i, arr[i]))
        #print(right_min)

        ans = 0
        for i in range(n):
            #print((right_min[i] - i) * (i - left_min[i]))
            ans += (right_min[i] - i) * (i - left_min[i]) * arr[i]
        return ans % (10**9 + 7)


        # 方法二：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        MOD = 10 ** 9 + 7
        n = len(arr)
        monoStack = []
        dp = [0] * n
        ans = 0
        for i, x in enumerate(arr):
            while monoStack and arr[monoStack[-1]] > x:
                monoStack.pop()
            k = i - monoStack[-1] if monoStack else i + 1
            dp[i] = k * x + (dp[i - k] if monoStack else 0)
            ans = (ans + dp[i]) % MOD
            monoStack.append(i)
        return ans





