"""
给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：
字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。
字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。

如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。

示例 1：
输入：start = "_L__R__R_", target = "L______RR"
输出：true
解释：可以从字符串 start 获得 target ，需要进行下面的移动：
- 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。
- 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。
- 将第二个片段向右移动散步，字符串现在变为 "L______RR" 。
可以从字符串 start 得到 target ，所以返回 true 。

示例 2：
输入：start = "R_L_", target = "__LR"
输出：false
解释：字符串 start 中的 'R' 片段可以向右移动一步得到 "_RL_" 。
但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。

示例 3：
输入：start = "_R", target = "R_"
输出：false
解释：字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。
 
提示：
n == start.length == target.length
1 <= n <= 10^5
start 和 target 由字符 'L'、'R' 和 '_' 组成

"""

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        # 方法一：模拟
        # 时间复杂度：
        # 空间复杂度：
        if start == target:
            return True
        
        count1, count2, count3, count4 = start.count('L'), start.count('R'), target.count('L'), target.count('R')
        #print('count1:', count1)
        #print('count2:', count2)
        #print('count3:', count3)
        #print('count4:', count4)
        if count1 != count3 or count2 != count4:
            #print('1')
            return False
        
        str1, str2 = "", ""
        order1, order2, order3, order4 = [], [], [], []
        for i in range(len(start)):
            if start[i] != "_":
                str1 += start[i]
                if start[i] == 'L':
                    order1.append(i)
                elif start[i] == 'R':
                    order2.append(i)
            if target[i] != "_":
                str2 += target[i]
                if target[i] == 'L':
                    order3.append(i)
                elif target[i] == 'R':
                    order4.append(i)
        #print('str1:', str1)
        #print('str2:', str2)
        if str1 != str2:
            print('2')
            return False
        
        #print('order1:', order1)
        #print('order2:', order2)
        #print('order3:', order3)
        #print('order4:', order4)
        for i in range(len(order1)):
            if order1[i] < order3[i]:
                #print('3')
                return False
        for i in range(len(order2)):
            if order2[i] > order4[i]:
                #print('4')
                return False
            
        return True
        
        
        
