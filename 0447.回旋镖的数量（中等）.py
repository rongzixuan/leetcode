"""
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。

"""

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        # 方法一：哈希表
        # 时间复杂度：O(n ^ 2)
        # 空间复杂度：O(n)       
        n = len(points)
        if n == 1:
            return 0

        res = 0
        for p in points:
            hashSet = defaultdict(int)
            for q in points:
                #print('p, q:', p, q)
                dist = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                #print('dist:', dist)
                #print('hashSet:', hashSet)
                if dist in hashSet:
                    #print('hashSet[dist]:', hashSet[dist])
                    res += 2 * hashSet[dist]
                hashSet[dist] += 1

        return res



