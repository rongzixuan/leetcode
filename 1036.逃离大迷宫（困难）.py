"""
在一个 106 x 106 的网格中，每个网格上方格的坐标为 (x, y) 。

现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。

每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。

只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。

示例 1：
输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
输出：false
解释：
从源方格无法到达目标方格，因为我们无法在网格中移动。
无法向北或者向东移动是因为方格禁止通行。
无法向南或者向西移动是因为不能走出网格。

示例 2：
输入：blocked = [], source = [0,0], target = [999999,999999]
输出：true
解释：
因为没有方格被封锁，所以一定可以到达目标方格。

提示：
0 <= blocked.length <= 200
blocked[i].length == 2
0 <= xi, yi < 10^6
source.length == target.length == 2
0 <= sx, sy, tx, ty < 10^6
source != target
题目数据保证 source 和 target 不在封锁列表内

"""


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:


        # 方法一：有限步数的广度优先搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(blocked)
        if n < 2:
            return True

        BLOCKED, VALID, FOUND = -1, 0, 1
        BOUNDRAY_LENGTH = 10**6
        
        blocked_set = set(tuple(bl) for bl in blocked)
        #print(blocked_set)

        def check(start: List[int], finish: List[int]) -> int:
            queue = [start]
            visited = {(start[0], start[1])}
            cutdown = n * (n - 1) // 2

            while queue and cutdown > 0:
                x1, y1 = queue.pop(0)
                for new_x, new_y in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
                    if 0 <= new_x < BOUNDRAY_LENGTH and 0 <= new_y < BOUNDRAY_LENGTH \
                    and (new_x, new_y) not in visited and (new_x, new_y) not in blocked_set:
                        if [new_x, new_y] == [finish[0], finish[1]]:
                            return FOUND
                        queue.append([new_x, new_y])
                        visited.add((new_x, new_y))
                        cutdown -= 1
                        #print('new_x, new_y:', new_x, new_y)
                        #print('cutdown:', cutdown)
                        #print('queue:', queue)
                        #print('visited:', visited)

            if cutdown > 0:
                #print('blocked')
                return BLOCKED
            return VALID


        if (result := check(source, target)) == FOUND:
            return True
        elif result == BLOCKED:
            #print('false1')
            return False
        else:
            result = check(target, source)
            if result == BLOCKED:
                #print('false2')
                return False
            return True


        # 方法二：离散化 + 广度优先搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(blocked)
        if n < 2:
            return True

        BOUNDRAY_LENGTH = 10 ** 6

        # 离散化
        rows = sorted(set(bl[0] for bl in blocked) | {source[0], target[0]})
        cols = sorted(set(bl[1] for bl in blocked) | {source[1], target[1]})
        r_mapping, c_mapping = dict(), dict()
        #print(rows)
        #print(cols)

        r_index = (0 if rows[0] == 0 else 1)
        #print(r_index)
        r_mapping[rows[0]] = r_index
        for i in range(1, len(rows)):
            r_index += (1 if rows[i] - rows[i - 1] == 1 else 2)
            r_mapping[rows[i]] = r_index
        if rows[-1] != BOUNDRAY_LENGTH - 1:
            r_index += 1

        c_index = (0 if cols[0] == 0 else 1)
        #print(c_index)
        c_mapping[cols[0]] = c_index
        for i in range(1, len(cols)):
            c_index += (1 if cols[i] - cols[i - 1] == 1 else 2)
            c_mapping[cols[i]] = c_index
        if cols[-1] != BOUNDRAY_LENGTH - 1:
            c_index += 1

        grid = [[0] * (c_index + 1) for _ in range(r_index + 1)]
        for x, y in blocked:
            grid[r_mapping[x]][c_mapping[y]] = 1

        x1, y1 = r_mapping[source[0]], c_mapping[source[1]]
        x2, y2 = r_mapping[target[0]], c_mapping[target[1]]

        queue = [[x1, y1]]
        grid[x1][y1] = 1
        while queue:
            x, y = queue.pop(0)
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= new_x <= r_index and 0 <= new_y <= c_index and grid[new_x][new_y] != 1:
                    if (new_x, new_y) == (x2, y2):
                        return True
                    queue.append([new_x, new_y])
                    grid[new_x][new_y] = 1

        return False






