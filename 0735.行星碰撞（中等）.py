"""
给定一个整数数组 asteroids，表示在同一行的行星。
对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

示例 1：
输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。

示例 2：
输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。

示例 3：
输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。

提示：
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid * stack[-1] > 0:  # 相同方向
                stack.append(asteroid)
            elif asteroid > 0:   # 方向不同，且向右
                stack.append(asteroid)
            elif asteroid < 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) > abs(asteroid):  # 被击碎
                    continue
                else:
                    while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
                        print('stack[-1]:', stack[-1])
                        stack.pop()
                    if not stack or asteroid * stack[-1] > 0:
                        stack.append(asteroid)
                    elif abs(stack[-1]) > abs(asteroid):
                        continue
                    elif abs(stack[-1]) == abs(asteroid):
                        stack.pop()
            #print(asteroid, stack)
        return stack


        # 方法二：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        stack = []
        for aster in asteroids:
            alive = True
            while alive and aster < 0 and stack and stack[-1] > 0:
                alive = stack[-1] < -aster
                if stack[-1] <= -aster:
                    stack.pop()
            if alive:
                stack.append(aster)
        return stack


