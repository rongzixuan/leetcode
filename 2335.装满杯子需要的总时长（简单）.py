"""
现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。

给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 最少 秒数。

示例 1：
输入：amount = [1,4,2]
输出：4
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。

示例 2：
输入：amount = [5,4,4]
输出：7
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。

示例 3：
输入：amount = [5,0,0]
输出：5
解释：每秒装满一杯冷水。

提示：
amount.length == 3
0 <= amount[i] <= 100

"""

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        
        # 2022/07/10      
        # 方法一：贪心
        # 时间复杂度：
        # 空间复杂度：
        from sortedcontainers import SortedList
        amount_list = SortedList()
        for a in amount:
            amount_list.add(a)
            
        ans = 0
        while amount_list[-1] > 0:
            #print(amount_list)
            if amount_list[1] == 0:
                ans += amount_list[-1]
                return ans
            else:
                tmp1, tmp2 = (amount_list[1] - 1), (amount_list[2] - 1)
                amount_list.pop()
                amount_list.pop()
                amount_list.add(tmp1)
                amount_list.add(tmp2)
                ans += 1
        return ans
   

        # 2023/02/11
        # 方法一：贪心 + 排序
        # 时间复杂度：
        # 空间复杂度：
        ans = 0
        amount.sort(reverse=True)
        while amount[0] > 0:
            #print(amount)
            amount[0] -= 1
            ans += 1
            if amount[1] > 0:
                amount[1] -= 1
            if amount[1] == amount[2] == 0:
                return ans + amount[0]
            else:
                amount.sort(reverse=True)
        return ans


        # 方法二：贪心 + 分类讨论
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        amount.sort()
        if (amount[0] + amount[1]) < amount[2]:
            return amount[2]
        else:
            total = sum(amount)
            return (total + 1) // 2
    
    
    
        
        
