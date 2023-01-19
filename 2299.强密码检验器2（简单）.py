"""
如果一个密码满足以下所有条件，我们称它是一个 强 密码：
它有至少 8 个字符。
至少包含 一个小写英文 字母。
至少包含 一个大写英文 字母。
至少包含 一个数字 。
至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。

给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。

示例 1：
输入：password = "IloveLe3tcode!"
输出：true
解释：密码满足所有的要求，所以我们返回 true 。

示例 2：
输入：password = "Me+You--IsMyDream"
输出：false
解释：密码不包含数字，且包含 2 个连续相同的字符。所以我们返回 false 。

示例 3：
输入：password = "1aB!"
输出：false
解释：密码不符合长度要求。所以我们返回 false 。
 
提示：
1 <= password.length <= 100
password 包含字母，数字和 "!@#$%^&*()-+" 这些特殊字符。

"""

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(password)
        if n < 8:
            return False

        lower_flag = False
        upper_flag = False
        num_flag = False
        signal_flag = False
        conti_flag = False

        for i, ch in enumerate(password):
            if i > 0 and ch == password[i - 1]:
                return False
            if ch.isalpha():
                if ord(ch) < 97:
                    upper_flag = True
                else:
                    lower_flag = True
            elif ch.isdigit():
                num_flag = True
            else:
                signal_flag = True
        return lower_flag and upper_flag and num_flag and signal_flag




