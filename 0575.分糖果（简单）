"""
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:


        # 方法一：贪心
        # 时间复杂度：O(n)
        # 时间复杂度：O(n)
        n = len(candyType)
        if n == 2:
            return 1

        count = len(set(candyType))
        return min(n // 2, count)
