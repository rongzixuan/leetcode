"""
给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。

对每位朋友 i，preferences[i] 包含一份 按亲近程度从高到低排列 的朋友列表。换句话说，排在列表前面的朋友与 i 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 0 到 n-1 之间的整数表示。

所有的朋友被分成几对，配对情况以列表 pairs 给出，其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi 配对。

但是，这样的配对情况可能会是其中部分朋友感到不开心。在 x 与 y 配对且 u 与 v 配对的情况下，如果同时满足下述两个条件，x 就会不开心：
x 与 u 的亲近程度胜过 x 与 y，且
u 与 x 的亲近程度胜过 u 与 v

返回 不开心的朋友的数目 。

"""

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:


        # 方法一：模拟
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        count = set()
        relation = [[0] * n for _ in range(n)] # 亲密关系的映射
        match = [0 for _ in range(n)]

        for i in range(n):
            for j in range(n-1):
                #print(i, j, preferences[i][j])
                relation[i][preferences[i][j]] = j + 1
        #print(relation)

        for x, y in pairs:
            match[x] = y
            match[y] = x
        #print(match)

        for i in range(n):
            x, y = i, match[i]
            for j in range(n):
                u, v = j, match[j]
                #print(x, y, u, v)
                if x != u and relation[x][y] > relation[x][u] and relation[u][v] > relation[u][x]:
                    #print(x, y, u, v)
                    #print('1111')
                    count.add(x)

        return len(count)





