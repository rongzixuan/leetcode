"""
我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

示例：
输入: 10
输出: 4

解释: 
在[1, 10]中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。
 
提示：
N 的取值范围是 [1, 10000]。

"""

class Solution:
    def rotatedDigits(self, n: int) -> int:


        # 方法一：模拟
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(C)
        # C = 7
        trans1 = {0: 0, 1: 1, 8: 8}
        trans2 = {2: 5, 5: 2, 6: 9, 9: 6}

        def judge(num):
            flag = False
            for ch in str(num):
                num = int(ch)
                if num not in trans1 and num not in trans2:
                    return False
                elif num in trans2:
                    flag = True
            return flag

        ans = 0
        for i in range(1, n + 1):
            if judge(i):
                ans += 1
        return ans


        # 方法二：数位动态规划
        # 时间复杂度：O(logn)
        # 空间复杂度：O(logn)
        DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)
        s = str(n)

        @cache
        def dfs(i: int, has_diff: bool, is_limit: bool) -> int:
            #print('i, has_diff, is_limit:', i, has_diff, is_limit)
            if i == len(s):
                return has_diff  # 只有包含 2/5/6/9 才算一个好数
            res = 0
            up = int(s[i]) if is_limit else 9
            #print('up:', up)
            for num in range(0, up + 1):  # 枚举要填入的数字 d
                if DIFFS[num] != -1:  # d 不是 3/4/7
                    #print('num:', num)
                    res += dfs(i + 1, has_diff or DIFFS[num], is_limit and num == up)
            return res

        ans = dfs(0, False, True)
        dfs.cache_clear()
        return ans





