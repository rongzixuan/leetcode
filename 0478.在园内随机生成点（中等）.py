"""
给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。

实现 Solution 类:
Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置 (x_center, y_center) 初始化对象
randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。

示例 1：
输入: 
["Solution","randPoint","randPoint","randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
解释:
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint ();//返回[-0.02493，-0.38077]
solution.randPoint ();//返回[0.82314,0.38945]
solution.randPoint ();//返回[0.36572,0.17248]
 
提示：
0 < radius <= 10^8
-10^7 <= x_center, y_center <= 10^7
randPoint 最多被调用 3 * 10^4 次

"""

# 方法一：拒绝采样
# 时间复杂度：O(1)
# 空间复杂度：O(1)
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            tmp_x = random.uniform(self.x - self.r, self.x + self.r)
            tmp_y = random.uniform(self.y - self.r, self.y + self.r)
            #print(tmp_x, tmp_y)
            if ((tmp_x - self.x) * (tmp_x - self.x) + (tmp_y - self.y) * (tmp_y - self.y))**0.5 <= self.r:
                return [tmp_x, tmp_y]


# 方法二：数学
# 时间复杂度：O(1)
# 空间复杂度：O(1)
import random
import math
class Solution:
    def __init__(self, radius: float, x_center: float, y_center:float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        new_r = random.uniform(0, 1)
        new_r = sqrt(new_r) * self.r
        #print(new_r)
        new_theta = random.random() * 2 * math.pi
        return [self.x + math.cos(new_theta) * new_r, self.y + math.sin(new_theta) * new_r]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()


