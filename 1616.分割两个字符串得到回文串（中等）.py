"""
给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。

当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。比方说， s = "abc" 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。

如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。

注意， x + y 表示连接字符串 x 和 y 。

示例 1：
输入：a = "x", b = "y"
输出：true
解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。

示例 2：
输入：a = "abdef", b = "fecab"
输出：true

示例 3：
输入：a = "ulacfd", b = "jizalu"
输出：true
解释：在下标为 3 处分割：
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。
 
提示：
1 <= a.length, b.length <= 10^5
a.length == b.length
a 和 b 都只包含小写英文字母

"""

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:


        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        def check(a, b):
            #print('a, b:', a, b)
            n = len(a)
            i, j = 0, n - 1
            flag, flag_a, flag_b = True, True, True
            while i < j:
                if flag: 
                    if a[i] != b[j]:
                        flag = False
                        if a[i] != a[j]:
                            flag_a = False
                        if b[i] != b[j]:
                            flag_b = False
                        if not flag_a and not flag_b:
                            return False
                    else:
                        i += 1
                        j -= 1                   
                elif not flag:
                    if flag_a and flag_b:
                        if b[i] != b[j] and a[i] != a[j]:
                            #print('i, j:', i, j)
                            return False 
                    elif flag_a:
                        if a[i] != a[j]:
                            return False
                    elif flag_b:
                        if b[i] != b[j]:
                            return False
                    i += 1
                    j -= 1              
            return True if i == j + 1 or i == j else False

        #res1 = check(a, b)
        #res2 = check(b, a)
        #print('res1:', res1)
        #print('res2:', res2)
        return check(a, b) or check(b, a)


        # 方法二：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        def check1(a: str, b: str) -> bool:
            i, j = 0, len(b) - 1
            while i < j and a[i] == b[j]:
                i, j = i + 1, j - 1
            return i >= j or check2(a, i, j) or check2(b, i, j)

        def check2(a: str, i: int, j: int) -> bool:
            return a[i: j + 1] == a[i: j + 1][::-1]

        return check1(a, b) or check1(b, a)






