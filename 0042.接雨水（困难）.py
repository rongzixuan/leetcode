"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

class Solution:
    def trap(self, height: List[int]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n ^ 2)
        # 空间复杂度：O(n)
        n = len(height)
        if n < 3:
            return 0

        dp_right = [i for i in range(n)]
        for i in range(1, n):
            if height[i] > height[i-1]:
                for j in range(i-1, -1, -1):
                    if height[i] <= height[dp_right[j]]:
                        break
                    dp_right[j] = i       
        #print('dp_right:', dp_right)

        dp_left = [i for i in range(n)]
        for i in range(n-2, -1, -1):
            if height[i] > height[i+1]:
                for j in range(i+1, n):
                    if height[i] <= height[dp_left[j]]:
                        break
                    dp_left[j] = i       
        #print('dp_left:', dp_left)

        res = sum([min(height[dp_left[i]], height[dp_right[i]]) - height[i] for i in range(1, n-1)])
        return res


        # 方法二：动态规划2
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(height)
        if n < 3:
            return 0

        dp_left = [height[i] for i in range(n)]
        for i in range(1, n):
            dp_left[i] = max(dp_left[i-1], dp_left[i])     
        #print('dp_left:', dp_left)

        dp_right = [height[i] for i in range(n)]
        for i in range(n-2, -1, -1):
            dp_right[i] = max(dp_right[i+1], dp_right[i])      
        #print('dp_right:', dp_right)

        res = sum([min(dp_left[i], dp_right[i]) - height[i] for i in range(1, n-1)])
        return res


        # 方法三：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(height)
        if n < 3:
            return 0

        left, right = 0, n-1
        max_left, max_right = height[0], height[n-1]

        res = 0
        while left < right:
            if height[left] <= height[right]:
                res += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                res += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])

        return res


        # 方法四：单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(height)
        if n < 3:
            return 0

        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                mid = stack.pop(-1)
                if not stack:
                    break
                left = stack[-1]
                cur_width = i - left - 1
                cur_height = min(height[i], height[left]) - height[mid]
                res += cur_height * cur_width
            stack.append(i)

        return res


    
    
