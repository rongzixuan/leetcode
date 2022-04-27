"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
    
    
        # 方法一：双指针
        # 时间复杂度：o(n)
        # 空间复杂度：o(n)
        n = len(s)
        left, right = 0, n - 1
        lowers = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a = []
        for i in range(n):
            a.append(s[i])
    
        while left < right:
            #print(left, right)
            while left < right and s[left] not in lowers:
                left += 1
                
            while left < right and s[right] not in lowers:
                right -= 1
                
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        
        #print(a)
        return ''.join(a)
            
    
    
    
