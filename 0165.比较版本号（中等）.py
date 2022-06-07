"""
给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。
比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

返回规则如下：
如果 version1 > version2 返回 1，
如果 version1 < version2 返回 -1，
除此之外返回 0。

"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:


        # 方法一：字符串分割
        # 时间复杂度：O(m+n)，其中m、n分别为version1和version2的长度
        # 空间复杂度：O(m+n)
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue = 0):
            x1, y1 = int(v1), int(v2)
            if x1 > y1:
                return 1
            elif x1 < y1:
                return -1

        return 0


        # 方法二：双指针
        # 时间复杂度：O(m+n)
        # 空间复杂度：O(1)
        m, n = len(version1), len(version2)
        v1, v2 = 0, 0

        while v1 <= m and v2 <= n:
            #print('v1, v2:', v1, v2)
            if v1 == m and v2 == n:
                return 0

            if v1 == m:
                num1 = 0
            else:
                tmp_v1 = v1
                while tmp_v1 < m and version1[tmp_v1] != '.':
                    tmp_v1 += 1
                num1 = int(version1[v1:tmp_v1])
                if tmp_v1 == m:
                    v1 = tmp_v1
                else:
                    v1 = tmp_v1 + 1

            if v2 == n:
                num2 = 0
            else:           
                tmp_v2 = v2
                while tmp_v2 < n and version2[tmp_v2] != '.':
                    tmp_v2 += 1
                num2 = int(version2[v2:tmp_v2])
                if tmp_v2 == n:
                    v2 = tmp_v2
                else:
                    v2 = tmp_v2 + 1

            #print('num1, num2:', num1, num2)
            #print('v1, v2:', v1, v2)
            if num1 != num2:
                return 1 if num1 > num2 else -1

        return 0


