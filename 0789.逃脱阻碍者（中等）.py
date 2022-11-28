"""
你在进行一个简化版的吃豆人游戏。你从 [0, 0] 点开始出发，你的目的地是 target = [xtarget, ytarget] 。地图上有一些阻碍者，以数组 ghosts 给出，第 i 个阻碍者从 ghosts[i] = [xi, yi] 出发。所有输入均为 整数坐标 。
每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 1 个单位 的新位置。当然，也可以选择 不动 。所有动作 同时 发生。
如果你可以在任何阻碍者抓住你 之前 到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。

只有在你有可能成功逃脱时，输出 true ；否则，输出 false 。

"""

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:


        # 方法一：曼哈顿距离
        # 时间复杂度：O(n),其中n为ghosts数组长度
        # 空间复杂度：O(1)
        def getManhattanDistance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        start = [0, 0]
        distance = getManhattanDistance(start, target)
        return all(getManhattanDistance(ghost, target) > distance for ghost in ghosts) 

    
    
    
