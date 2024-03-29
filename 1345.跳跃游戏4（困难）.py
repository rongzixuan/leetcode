"""
给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。

每一步，你可以从下标 i 跳到下标：
i + 1 满足：i + 1 < arr.length
i - 1 满足：i - 1 >= 0
j 满足：arr[i] == arr[j] 且 i != j

请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。

注意：任何时候你都不能跳到数组外面。

示例 1：
输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
输出：3
解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。

示例 2：
输入：arr = [7]
输出：0
解释：一开始就在最后一个元素处，所以你不需要跳跃。

示例 3：
输入：arr = [7,6,9,6,9,6,9,7]
输出：1
解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。

示例 4：
输入：arr = [6,1,9]
输出：2

示例 5：
输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
输出：3
 
提示：
1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8

"""


class Solution:
    def minJumps(self, arr: List[int]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(arr)
        if n == 1:
            return 0
        elif arr[0] == arr[-1]:
            return 1

        from collections import defaultdict
        arr_dict = defaultdict(list)
        for i, a in enumerate(arr):
            arr_dict[a].append(i)
        #print(arr_dict)

        #queue = [(0, arr[0], 0)]
        queue = deque()
        queue.append((0, arr[0], 0))
        visited = {0}
        #visited.add(0)
        while queue:
            #i, a, step = queue.pop(0)
            i, a, step = queue.popleft()
            if i == n - 1:
                return step
            """if a == arr[-1]:
                return step if i == n - 1 else step + 1"""
            for j in arr_dict[a]:
                if j not in visited:
                    queue.append((j, arr[j], step + 1))
                    visited.add(j)
            del arr_dict[a]           
            if i < n - 1 and (i + 1) not in visited:
                queue.append((i + 1, arr[i + 1], step + 1))
                visited.add(i + 1)
            if i > 0 and (i - 1) not in visited:
                queue.append((i - 1, arr[i - 1], step + 1))
                visited.add(i - 1)


                
                
                
