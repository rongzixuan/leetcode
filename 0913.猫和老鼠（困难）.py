"""
两位玩家分别扮演猫和老鼠，在一张 无向 图上进行游戏，两人轮流行动。

图的形式是：graph[a] 是一个列表，由满足 ab 是图中的一条边的所有节点 b 组成。

老鼠从节点 1 开始，第一个出发；猫从节点 2 开始，第二个出发。在节点 0 处有一个洞。

在每个玩家的行动中，他们 必须 沿着图中与所在当前位置连通的一条边移动。例如，如果老鼠在节点 1 ，那么它必须移动到 graph[1] 中的任一节点。

此外，猫无法移动到洞中（节点 0）。

然后，游戏在出现以下三种情形之一时结束：
如果猫和老鼠出现在同一个节点，猫获胜。
如果老鼠到达洞中，老鼠获胜。
如果某一位置重复出现（即，玩家的位置和移动顺序都与上一次行动相同），游戏平局。

给你一张图 graph ，并假设两位玩家都都以最佳状态参与游戏：
如果老鼠获胜，则返回 1；
如果猫获胜，则返回 2；
如果平局，则返回 0 。
 
示例 1：
输入：graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
输出：0

示例 2：
输入：graph = [[1,3],[0],[3],[0,2]]
输出：1

提示：
3 <= graph.length <= 50
1 <= graph[i].length < graph.length
0 <= graph[i][j] < graph.length
graph[i][j] != i
graph[i] 互不相同
猫和老鼠在游戏中总是移动

"""


DRAW = 0       # 平局
MOUSE_WIN = 1  # 老鼠获胜
CAT_WIN = 2    # 猫获胜

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n^4)
        # 空间复杂度：O(n^3)
        n = len(graph)
        dp = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]

        def getRes(mouse, cat, turn):
            if turn >= 2 * n:
                return DRAW     

            res = dp[mouse][cat][turn]
            if res != -1:
                return res
            if mouse == 0:
                res = MOUSE_WIN      
            elif mouse == cat:
                res = CAT_WIN                  
            else:
                res = getNextRes(mouse, cat, turn)  
            dp[mouse][cat][turn] = res 
            return res

        def getNextRes(mouse, cat, turn):
            curMove = mouse if turn % 2 == 0 else cat
            defaultRes = MOUSE_WIN if curMove == cat else CAT_WIN
            res = defaultRes
            for nxt in graph[curMove]:
                if curMove == cat and nxt == 0:
                    continue
                nextMouse = mouse if curMove == cat else nxt
                nexCat = cat if curMove == mouse else nxt
                nextRes = getRes(nextMouse, nexCat, turn + 1)
                if nextRes != defaultRes:
                    res = nextRes
                    if res != DRAW:
                        break
            return res

        return getRes(1, 2, 0)     




