"""
现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。
给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

字符串 s 字典顺序小于 字符串 t 有两种情况：
在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
 
示例 1：
输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"

示例 2：
输入：words = ["z","x"]
输出："zx"

示例 3：
输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。

提示：
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] 仅由小写英文字母组成
 
注意：本题与主站 269 题相同： https://leetcode-cn.com/problems/alien-dictionary/

"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:


        # 方法一：拓扑排序 + 深度优先搜索
        # 时间复杂度：O(n * d + C)
        # 空间复杂度：O(n + C)
        # n = len(words)
        # d 为word的平均长度
        # C = 字典中字符个数
        # 拓扑排序
        graph = {}
        for c in words[0]:
            graph[c] = []
        #print(graph)
        for pre, nxt in pairwise(words):
            #print(pre, nxt)
            for ch in nxt:
                graph.setdefault(ch, [])
            for u, v in zip(pre, nxt):
                #print(u, v)
                if u != v:
                    graph[u].append(v)
                    break
            else:
                if len(pre) > len(nxt):
                    return ""
        #print(graph)

        # 深度优先搜索
        VISITING, VISITED = 1, 2
        states = {}
        order = []
        def dfs(u: str) -> bool:
            #print('order before:', order, u)
            #print('states before:', states, u)
            states[u] = VISITING
            for v in graph[u]:
                if v not in states:
                    if not dfs(v):
                        #print(u, 'false')
                        return False
                elif states[v] == VISITING:
                    #print(u, 'false')
                    return False
            order.append(u)
            states[u] = VISITED
            #print(u, 'true')
            #print('order after:', order, u)
            #print('states after:', states, u)
            return True
        #print('order outside:', order)
        #print('states outside:', states)
        return ''.join(reversed(order)) if all(dfs(u) for u in graph if u not in states) else ""


        # 方法二：拓扑排序 + 广度优先搜索
        # 时间复杂度：O(n * d + C)
        # 空间复杂度：O(n + C)
        # n = len(words)
        # d 为word的平均长度
        # C = 字典中字符个数
        graph = defaultdict(list)
        inDeg = {ch: 0 for ch in words[0]}
        for pre, nxt in pairwise(words):
            for ch in nxt:
                inDeg.setdefault(ch, 0)
            for u, v in zip(pre, nxt):
                if u != v:
                    graph[u].append(v)
                    inDeg[v] += 1
                    break
            else:
                if len(pre) > len(nxt):
                    return ""
        #print(graph)
        #print(inDeg)

        queue = [u for u, d in inDeg.items() if d == 0]
        for u in queue:
            for v in graph[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    queue.append(v)
        #print(queue)
        return ''.join(queue) if len(queue) == len(inDeg) else ""


