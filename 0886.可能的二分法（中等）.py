"""
给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。

示例 1：
输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]

示例 2：
输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false

示例 3：
输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
 
提示：
1 <= n <= 2000
0 <= dislikes.length <= 10^4
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
dislikes 中每一组都 不同

"""

class Union:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.height = [0] * (n + 1)

    def find(self, x):
        parent = self.parents[x]
        while parent != self.parents[x]:
            parent = self.parents[x]
        return parent

    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        height1, height2 = self.height[x], self.height[y]
        if height1 > height2:
            self.parents[y] = x
        elif height1 < height2:
            self.parents[x] = y
        else:
            self.parents[y] = x
            self.height[x] + 1

    def isMerge(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(n + m)
        dis = defaultdict(list)
        for i, j in dislikes:
            dis[i].append(j)
            dis[j].append(i)
        #print(dis)
        groups = [-1] * n  # 所属组别
        
        def dfs(i, group):
            #print(i, group)
            if groups[i - 1] == -1:
                groups[i - 1] = group
            for j in dis[i]:
                if groups[j - 1] == groups[i - 1]:
                    #print(i, j)
                    return False
                if groups[j - 1] == -1:
                    if not dfs(j, 1 - group):
                        return False
            return True
       
        ans = True 
        for i in range(1, n + 1):
            if not dfs(i, 0):
                ans = False
        #print(groups)
        return False if not ans else True


        # 方法二：广度优先搜索
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(n + m)
        dis = defaultdict(list)
        for i, j in dislikes:
            dis[i].append(j)
            dis[j].append(i)
        #print(dis)
        groups = [-1] * n  # 所属组别

        stack = []
        for i in range(1, n + 1):
            if groups[i - 1] == -1:
                groups[i - 1] = 0
                stack.append((i, 0))
            while stack:
                i, group = stack.pop(0)
                for j in dis[i]:
                    if groups[j - 1] == -1:
                        stack.append((j, 1 - group))
                        groups[j - 1] = 1 - group
                    elif groups[j - 1] == group:
                        return False
        return True


        # 方法三：深度优先搜索
        # 时间复杂度：O(n + m)
        # 空间复杂度：O(n + m)
        dis = defaultdict(list)
        for i, j in dislikes:
            dis[i].append(j)
            dis[j].append(i)
        #print(dis)
        groups = [-1] * n  # 所属组别

        stack = []
        for i in range(1, n + 1):
            if groups[i - 1] == -1:
                groups[i - 1] = 0
                stack.append((i, 0))
            while stack:
                i, group = stack.pop(-1)
                for j in dis[i]:
                    if groups[j - 1] == -1:
                        stack.append((j, 1 - group))
                        groups[j - 1] = 1 - group
                    elif groups[j - 1] == group:
                        return False
        return True


        # 方法四：并查集
        # 时间复杂度：O(n + ma(n))
        # 空间复杂度：O(n + m)
        # ma为反Ackerman函数 
        dis = defaultdict(list)
        for i, j in dislikes:
            dis[i].append(j)
            dis[j].append(i)
        #print(dis)
        groups = [-1] * n  # 所属组别

        union = Union(n)
        for i in range(1, n + 1):
            if len(dis[i]) > 0:
                first = dis[i][0]
            for j in dis[i]:
                union.merge(j, first)
                if union.isMerge(j, i):
                    return False
        return True




