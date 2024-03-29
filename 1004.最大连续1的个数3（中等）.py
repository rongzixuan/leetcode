"""
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

示例 1：
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 
提示：
1 <= nums.length <= 10^5
nums[i] 不是 0 就是 1
0 <= k <= nums.length

"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        # 方法一：滑动窗口
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        left = 0
        ans = 0
        count = 0

        for right in range(n):
            count += (nums[right] == 0)
            while count > k:
                count -= (nums[left] == 0)
                left += 1
            ans = max(ans, right - left + 1)

        return ans


        # 方法二：二分查找
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(nums)
        count = [0] * (n + 1)
        count[0] = 0
        for i in range(1, n + 1):
            count[i] = count[i - 1] + (1 - nums[i - 1])
        #print(count)

        ans = 0
        for j in range(n): 
            #print('i, j:', i, j)
            i = bisect.bisect_left(count, count[j + 1] - k)
            ans = max(ans, j - i + 1) 
            print('i, j, ans:', i, j, ans)
            #print('ans:', ans)

        return ans


        # 方法三：二分查找
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(nums)
        count = [0] * (n + 1)
        count[0] = 0
        for i in range(1, n + 1):
            count[i] = count[i - 1] + (1 - nums[i - 1])
        #print(count)

        ans = 0
        for j in range(n): 
            #print('i, j:', i, j)
            left, right = 0, n          
            while left < right:
                mid = left + (right - left) // 2
                #print('left, mid, right:', left, mid, right)
                if count[j + 1] - count[mid] == k:
                    right = mid
                elif count[j + 1] - count[mid] < k:
                    right = mid
                elif count[j + 1] - count[mid] > k:
                    left = mid + 1
            #print('j, left, mid, right:', j, left, mid, right)
       
            ans = max(ans, j - left + 1) 
            #print('ans:', ans)

        return ans 





