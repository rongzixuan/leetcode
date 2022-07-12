"""
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。

给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。

示例 1：
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1

示例 2：
输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2

示例 3：
输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3

提示：
start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成

"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(n)
        # n = len(bank)
        # m = len(start)
        n = len(bank)
        queue = [(start, 0)]
        visited = set(start)
        #bank_set = set(bank)

        while queue:
            node, times = queue.pop(0)
            #print(node, end)
            if node == end:
                return times
            for next_node in bank:
                if next_node != node and next_node not in visited:
                    count = 0
                    for i in range(8):
                        if node[i] != next_node[i]:
                            count += 1
                        if count > 1:
                            break
                    #print(next_node, count)
                    if count == 1:
                        queue.append((next_node, times + 1))
                        visited.add(next_node)

        return -1


        # 方法二：预处理 + 广度优先搜索
        # 时间复杂度：O()
        # 空间复杂度：O(n)
        # n = len(bank)
        # m = len(start)
        if start == end:
            return 0

        def diffOne(s: str, t: str) -> bool:
            return sum(x != y for x, y in zip(s, t)) == 1

        m = len(bank)
        adj = [[] for _ in range(m)]
        endIndex = -1
        for i, s in enumerate(bank):
            if s == end:
                endIndex = i
            for j in range(i + 1, m):
                if diffOne(s, bank[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        if endIndex == -1:
            return -1

        q = [i for i, s in enumerate(bank) if diffOne(start, s)]
        vis = set(q)
        step = 1
        while q:
            tmp = q
            q = []
            for cur in tmp:
                if cur == endIndex:
                    return step
                for nxt in adj[cur]:
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
            step += 1
        return -1



