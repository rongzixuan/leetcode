"""
给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：
pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

注意 ^ 表示 按位异或（bitwise-xor）运算。

可以证明答案是 唯一 的。

示例 1：
输入：pref = [5,2,0,3,1]
输出：[5,7,2,3,2]
解释：从数组 [5,7,2,3,2] 可以得到如下结果：
- pref[0] = 5
- pref[1] = 5 ^ 7 = 2
- pref[2] = 5 ^ 7 ^ 2 = 0
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1

示例 2：
输入：pref = [13]
输出：[13]
解释：pref[0] = arr[0] = 13
 
提示：
1 <= pref.length <= 10^5
0 <= pref[i] <= 10^6

"""

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        
        # 方法一：位运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(pref)
        arr = [pref[0]] * n
        
        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]
        return arr
    
    
