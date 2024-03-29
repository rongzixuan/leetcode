"""
给你一个字符串 s ，根据下述规则反转字符串：
所有非英文字母保留在原有位置。
所有英文字母（小写或大写）位置反转。

返回反转后的 s 。

示例 1：
输入：s = "ab-cd"
输出："dc-ba"

示例 2：
输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入：s = "Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 
提示
1 <= s.length <= 100
s 仅由 ASCII 值在范围 [33, 122] 的字符组成
s 不含 '\"' 或 '\\'

"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:


        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(s)
        arr = list(s)
        #print(arr)

        left, right = 0, n - 1
        while left < right:
            #print(left, right)
            while left < right and not arr[left].isalpha():
                left += 1
            while left < right and not arr[right].isalpha():
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return ''.join(arr)


