"""
有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。

你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。

举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.

请返回一个能打开保险箱的最短字符串。

 
示例1:
输入: n = 1, k = 2
输出: "01"
说明: "10"也可以打开保险箱。
 
示例2:
输入: n = 2, k = 2
输出: "00110"
说明: "01100", "10011", "11001" 也能打开保险箱。
 
提示：
n 的范围是 [1, 4]。
k 的范围是 [1, 10]。
k^n 最大可能为 4096。

"""

class Solution:
    def crackSafe(self, n: int, k: int) -> str:


        # 方法一：欧拉回路 + dfs
        # 时间复杂度：O(n * k**n)
        # 空间复杂度：O(n * k**n)
        used = set()
        ans = list()
        highest = 10 ** (n - 1)
        #print('highest:', highest)

        def dfs(node: int):
            #print('node:', node)
            #print('ans:', ans)
            for i in range(k):
                new_node = node * 10 + i
                #print('i, new_node:', i, new_node)
                if new_node not in used: 
                    #print('yes')
                    used.add(new_node)
                    dfs(new_node % highest)
                    ans.append(str(i))
                    #print('ans:', ans)

        dfs(0)
        #print('ans1:', ans)
        return "".join(ans) + "0" * (n - 1)


        # 方法二：欧拉回路 + bfs
        # 时间复杂度：O(n * k**n)
        # 空间复杂度：O(n * k**n)
        ans = list()
        nodeNum = k**(n-1)
        edges = [k-1] * nodeNum
        #print('edges:', edges)

        node = 0
        while edges[node] >= 0:
            #print('node before:', node)
            edge = edges[node]
            #print('edge:', edge)
            edges[node] -= 1
            node = (node * k + edge) % nodeNum
            #print('node after:', node)
            ans.append(str(edge))
    
        return  "0" * (n-1)  + "".join(ans)





