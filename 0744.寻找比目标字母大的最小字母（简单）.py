"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：
如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

示例 1：
输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"

示例 2:
输入: letters = ["c","f","j"], target = "c"
输出: "f"

示例 3:
输入: letters = ["c","f","j"], target = "d"
输出: "f"
 
提示：
2 <= letters.length <= 10^4
letters[i] 是一个小写字母
letters 按非递减顺序排序
letters 最少包含两个不同的字母
target 是一个小写字母

"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:


        # 方法一：遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(letters)
        for letter in letters:
            if letter > target:
                return letter

        return letters[0]


        # 方法二：遍历2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        return next((letter for letter in letters if letter > target), letters[0])


        # 方法三：遍历3
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        return next(iter(letter for letter in letters if letter > target), letters[0])


        # 方法四：遍历4
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        return next(iter([letter for letter in letters if letter > target]), letters[0])


        # 方法五：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(letters)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1 
            elif letters[mid] > target:
                right = mid
        
        return letters[left] if letters[left] > target else letters[0]


        # 方法六：二分法2
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        from bisect import bisect_right
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]




