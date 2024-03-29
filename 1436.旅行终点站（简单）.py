"""
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。

"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(paths)
        if n == 1:
            return paths[0][1]

        from collections import defaultdict
        hash_table = defaultdict(int)
        #hash_table = {}
        #print(hash_table)

        for i in range(n):
            hash_table[paths[i][0]] += 1
            hash_table[paths[i][1]] -= 1
        #print(hash_table)

        for k, v in hash_table.items():
            if v == -1:
                return k


        # 方法二：哈希表
        # 时间复杂度：O(mn)
        # 空间复杂度：O(mn)，m为地点字符串的最大长度
        path1 = {path[0] for path in paths}

        return next(path[1] for path in paths if path[1] not in path1)





