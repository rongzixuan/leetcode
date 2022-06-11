"""
如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。
给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。
返回使 s 单调递增的最小翻转次数。

示例 1：
输入：s = "00110"
输出：1
解释：翻转最后一位得到 00111.

示例 2：
输入：s = "010110"
输出：2
解释：翻转得到 011111，或者是 000111。

示例 3：
输入：s = "00011000"
输出：2
解释：翻转得到 00000000。

提示：
1 <= s.length <= 10^5
s[i] 为 '0' 或 '1'

"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:


        # 方法一：模拟 + 贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        count0, count1 = s.count('0'), s.count('1')
        count = [count0]

        # 以i为0、1分界线
        for i, ch in enumerate(s):
            if ch == '0':
                count0 -= 1
            else:
                count0 += 1
            count.append(count0)
        return min(count)


        # 方法二：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        count0, count1 = s.count('0'), 0
        n = len(s)
        ans = count0

        # 以i为0、1分界线
        for i, ch in enumerate(s):
            if ch == '0':
                count0 -= 1
            else:
                count0 += 1
            ans = min(ans, count0 + count1)
        return ans


        # 方法三：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        dp0, dp1 = 0, 0

        # 以i为0、1分界线
        for i, ch in enumerate(s):
            tmp_dp0, tmp_dp1 = dp0, min(dp0, dp1)
            if ch == '1':
                tmp_dp0 += 1
            else:
                tmp_dp1 += 1
            dp0, dp1 = tmp_dp0, tmp_dp1
        return min(dp0, dp1)


        # 方法四：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        cnt0 = s.count('0')
        cnt = cnt0
        dp = [[0, cnt0]] # [左边1的个数, 右边0的个数]

        for i in s:
            if i == '1':
                dp.append([dp[-1][0]+1, dp[-1][1]]) # 左边1的个数加1
            else:
                dp.append([dp[-1][0], dp[-1][1]-1]) # 右边0的个数减1
            cnt = min(cnt, sum(dp[-1]))
        return cnt    


