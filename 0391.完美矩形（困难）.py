"""
给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。

如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
 
示例 1：
输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
输出：true
解释：5 个矩形一起可以精确地覆盖一个矩形区域。 

示例 2：
输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
输出：false
解释：两个矩形之间有间隔，无法覆盖成一个矩形。

示例 3：
输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]
输出：false
解释：图形顶端留有空缺，无法覆盖成一个矩形。

示例 4：
输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
输出：false
解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。

提示：
1 <= rectangles.length <= 2 * 10^4
rectangles[i].length == 4
-10^5 <= xi, yi, ai, bi <= 10^5

"""

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        # 方法一：遍历 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(rectangles)
        if n == 1:
            return True

        hash_table = set()
        area_sum = 0
        min_x, min_y, max_a, max_b = float('inf'), float('inf'), float('-inf'), float('-inf')
        for x, y, a, b in rectangles:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            area_sum += (a - x) * (b - y)

            if (x, y) in hash_table:
                hash_table.remove((x, y))
            else:
                hash_table.add((x, y))

            if (x, b) in hash_table:
                hash_table.remove((x, b))
            else:
                hash_table.add((x, b))

            if (a, y) in hash_table:
                hash_table.remove((a, y))
            else:
                hash_table.add((a, y))

            if (a, b) in hash_table:
                hash_table.remove((a, b))
            else:
                hash_table.add((a, b))          

        #print(min_x, min_y, max_a, max_b)
        #print(area_sum)
        #print(hash_table)
        return area_sum == (max_a - min_x) * (max_b - min_y) \
                and len(hash_table) == 4 \
                and (min_x, min_y) in hash_table \
                and (min_x, max_b) in hash_table \
                and (max_a, min_y) in hash_table \
                and (max_a, max_b) in hash_table 


