"""
在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。

 
示例 1:
输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
解释:

示例 2:
输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]

解释:
即使树都在一条直线上，你也需要先用绳子包围它们。
 
注意:
所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
输入的整数在 0 到 100 之间。
花园至少有一棵树。
所有树的坐标都是不同的。
输入的点没有顺序。输出顺序也没有要求。

"""


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:


        # 方法一：Javis算法（求凸包）
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        def cross(x, y, z):  # 求外积
            return (y[0] - x[0]) * (z[1] - y[1]) - (z[0] - y[0]) * (y[1] - x[1])

        n = len(trees)
        if n <= 3:
            return trees

        left = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[left][0]:
                left = i

        x = left
        visited = set()
        res = []
        while True:
            y = (x + 1) % n
            for z in range(n):
                #if z not in visited:
                if cross(trees[x], trees[y], trees[z]) < 0:
                    y = z

            if y not in visited:
                visited.add(y)
                res.append(trees[y])

            for z in range(n):
                if z != x and z != y and cross(trees[x], trees[y], trees[z]) == 0 and z not in visited:
                    visited.add(z)
                    res.append(trees[z])

            if y == left:
                break
            x = y

        return res


        # 方法二：Graham算法（求凸包）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        def cross(x, y, z):  # 求外积
            return (y[0] - x[0]) * (z[1] - y[1]) - (z[0] - y[0]) * (y[1] - x[1])

        def distance(x, y):  # 求距离
            return (y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2

        n = len(trees)
        if n <= 3:
            return trees

        bottom = 0  # y最小的点
        for i, tree in enumerate(trees):
            if tree[1] < trees[bottom][1]:
                bottom = i
        trees[bottom], trees[0] = trees[0], trees[bottom]

        # 以 bottom 原点，按照极坐标的角度大小进行排序
        def cmp(x: List[int], y: List[int]) -> int:
            diff = cross(trees[0], y, x) - cross(trees[0], x, y)
            return diff if diff else distance(trees[0], x) - distance(trees[0], y)
        trees[1:] = sorted(trees[1:], key=cmp_to_key(cmp))
        #print('trees1:', trees)
        #print(cross([2, 0], [2, 2], [4, 2]))
        #print(cross([2, 0], [2, 2], [3, 3]))

        # 对于凸包最后且在同一条直线的元素按照距离从大到小进行排序
        r = n - 1
        while r >= 0 and cross(trees[0], trees[n - 1], trees[r]) == 0:
            r -= 1
        l, h = r + 1, n - 1
        while l < h:
            trees[l], trees[h] = trees[h], trees[l]
            l += 1
            h -= 1
        #print('trees2:', trees)

        stack = [0, 1]
        for i in range(2, n):
            # 如果当前元素与栈顶的两个元素构成的向量顺时针旋转，则弹出栈顶元素
            while len(stack) > 1 and cross(trees[stack[-2]], trees[stack[-1]], trees[i]) < 0:
                stack.pop()
            stack.append(i)
        return [trees[i] for i in stack]


        # 方法三：Andrew算法（求凸包）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        trees.sort()
        #print('trees1:', trees)

        hull = [0]  # hull[0] 需要入栈两次，不标记
        used = [False] * n
        # 求凸包的下半部分
        for i in range(1, n):
            while len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        #print('trees2:', trees)
        #print('hull1:', hull)

        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(hull) > m and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        #print('trees3:', trees)
        #print('hull2:', hull)
        # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        hull.pop()

        return [trees[i] for i in hull]












