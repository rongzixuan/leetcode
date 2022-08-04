"""
给你一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示网格上圆心为 (xi, yi) 且半径为 ri 的第 i 个圆，返回出现在 至少一个 圆内的 格点数目 。

注意：
格点 是指整数坐标对应的点。
圆周上的点 也被视为出现在圆内的点。
 
示例 1：
输入：circles = [[2,2,1]]
输出：5
解释：
给定的圆如上图所示。
出现在圆内的格点为 (1, 2)、(2, 1)、(2, 2)、(2, 3) 和 (3, 2)，在图中用绿色标识。
像 (1, 1) 和 (1, 3) 这样用红色标识的点，并未出现在圆内。
因此，出现在至少一个圆内的格点数目是 5 。

示例 2：
输入：circles = [[2,2,2],[3,4,1]]
输出：16
解释：
给定的圆如上图所示。
共有 16 个格点出现在至少一个圆内。
其中部分点的坐标是 (0, 2)、(2, 0)、(2, 4)、(3, 2) 和 (4, 4) 。

提示：
1 <= circles.length <= 200
circles[i].length == 3
1 <= xi, yi <= 100
1 <= ri <= min(xi, yi)

"""

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        
        # 方法一：多源广度优先搜索（超时）
        # 时间复杂度：
        # 空间复杂度：
        n = len(circles)
        ans = set()
        
        queue = deque([])
        visited = set()
        for x, y, r in circles:
            queue.append((x, y, r, x, y, 0))
            ans.add((x, y))
            visited.add((x, y))
        
        while queue:
            length = len(queue)
            for _ in range(length):
                circle_x, circle_y, circle_r, x, y, d = queue.popleft()
                for new_x, new_y in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
                    if (new_x, new_y) not in visited:
                        new_d = ((new_x - circle_x) ** 2 + (new_y - circle_y) ** 2) ** 0.5
                        if new_d <= circle_r:
                            ans.add((new_x, new_y))
                            queue.append((circle_x, circle_y, circle_r, new_x, new_y, new_d))
                            visited.add((new_x, new_y))
        #print(ans)                       
        return len(ans)
    
    
        # 方法二：广度优先搜索（超时）
        # 时间复杂度：
        # 空间复杂度：
        n = len(circles)
        ans = set()
        visited = set()
        
        queue = deque([])       
        for x_old, y_old, r_old in circles:
            queue.append((x_old, y_old, r_old, x_old, y_old, 0))
            ans.add((x_old, y_old))
            visited.add((x_old, y_old))
        
            while queue:
                length = len(queue)
                for _ in range(length):
                    circle_x, circle_y, circle_r, x, y, d = queue.popleft()
                    for new_x, new_y in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
                        if (new_x, new_y) not in ans:
                            new_d = ((new_x - circle_x) ** 2 + (new_y - circle_y) ** 2) ** 0.5
                            if new_d <= circle_r:
                                ans.add((new_x, new_y))
                                queue.append((circle_x, circle_y, circle_r, new_x, new_y, new_d))
                                visited.add((new_x, new_y))
            queue = deque([])
            visited = set()
            
        #print(ans)                        
        return len(ans)
        
        
        # 方法三：模拟
        # 时间复杂度：
        # 空间复杂度：
        n = len(circles)
        ans = set()
        
        for i, circle in enumerate(circles):
            x, y, r = circle[0], circle[1], circle[2]
            up, down, left, right = y + r, y - r, x - r, x + r
            for new_x in range(left, right + 1):
                for new_y in range(down, up + 1):
                    if (new_x, new_y) not in ans:
                        new_d = ((new_x - x) ** 2 + (new_y - y) ** 2) ** 0.5
                        if new_d <= r:
                            ans.add((new_x, new_y))
                            
        return len(ans)
            
            
            
            
            
                        
