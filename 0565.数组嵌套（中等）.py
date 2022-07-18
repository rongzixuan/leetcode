"""
索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。
假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

示例 1:
输入: A = [5,4,0,3,1,6,2]
输出: 4

解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0} 

提示：
1 <= nums.length <= 10^5
0 <= nums[i] < nums.length
A中不含有重复的元素。

"""

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:


        # 方法一：有向图模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        max_length = 0
        visited = set()
        n = len(nums)
        for i in range(n):
            v = nums[i]
            visited.add(i)
            length = 1
            while v != i and v not in visited:
                visited.add(v)
                v = nums[v]
                length += 1
            max_length = max(max_length, length)

        return max_length


        # 方法二：有向图模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        max_length = 0
        visited = set()
        n = len(nums)
        for i in range(n):
            length = 0
            while i not in visited:
                visited.add(i)
                i = nums[i]
                length += 1
            max_length = max(max_length, length)

        return max_length


        # 方法三：原地修改
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        max_length = 1

        for i in range(n):
            tmp_i = i
            length = 0
            while nums[tmp_i] != tmp_i:
                v = nums[tmp_i]
                nums[tmp_i] = i
                tmp_i = v
                length += 1
            max_length = max(max_length, length)

        return max_length



