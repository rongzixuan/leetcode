"""
n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。

每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。

就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。

给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：

dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
返回表示最终状态的字符串。

 
示例 1：
输入：dominoes = "RR.L"
输出："RR.L"
解释：第一张多米诺骨牌没有给第二张施加额外的力。

示例 2：
输入：dominoes = ".L.R...LR..L.."
输出："LL.RR.LLRRLL.."
 

提示：
n == dominoes.length
1 <= n <= 10^5
dominoes[i] 为 'L'、'R' 或 '.'

"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:


        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(dominoes)
        from collections import deque
        queue = deque()
        time = [-1] * n
        force = [[] for _ in range(n)]
        for i in range(n):
            if dominoes[i] != '.':
                queue.append(i)
                time[i] = 0
                force[i].append(dominoes[i])

        res = ['.'] * n
        while queue:
            i = queue.popleft()
            if len(force[i]) == 1:
                res[i] = force[i][0]
                new_i = i - 1 if force[i][0] == 'L' else i + 1
                if 0 <= new_i < n:
                    if time[new_i] == -1:
                        time[new_i] = time[i] + 1
                        force[new_i].append(force[i][0])  
                        queue.append(new_i)                      
                    elif time[new_i] == time[i] + 1:
                        force[new_i].append(force[i][0])                   

        return ''.join(res)


        # 方法二：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O()
        n = len(dominoes)





