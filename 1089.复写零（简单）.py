"""
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。
要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

示例 1：
输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

示例 2：
输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]

提示：
1 <= arr.length <= 10000
0 <= arr[i] <= 9

"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0:
                #print(i)
                #print(arr[:i + 1], [0], arr[i + 1: -1])
                arr.insert(i + 1, 0)
                arr.pop()
                i += 1
            i += 1
            #print(arr)


        # 方法二：正反遍历 + 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(arr)
        count = 0
        i, j = 0, 0
        while j < n:
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1
        #print(i, j)
        double = True if (j - n) % 2 == 0 else False
        #print(double)
        i, j = i - 1, n - 1
        

        while i >= 0 and j >= 0:
            #print(i, j)
            if arr[i] == 0 and double:
                arr[j] = 0
                arr[j - 1] = 0
                i -= 1
                j -= 2               
            else:
                arr[j] = arr[i]
                i -= 1
                j -= 1
            double = True


