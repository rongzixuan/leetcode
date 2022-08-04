"""
给你一个整数数组 cards ，其中 cards[i] 表示第 i 张卡牌的 值 。如果两张卡牌的值相同，则认为这一对卡牌 匹配 。

返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 -1 。

示例 1：
输入：cards = [3,4,2,3,4,7]
输出：4
解释：拿起卡牌 [3,4,2,3] 将会包含一对值为 3 的匹配卡牌。注意，拿起 [4,2,3,4] 也是最优方案。

示例 2：
输入：cards = [1,0,5,3]
输出：-1
解释：无法找出含一对匹配卡牌的一组连续卡牌。
 
提示：
1 <= cards.length <= 10^5
0 <= cards[i] <= 10^6

"""


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        
        # 方法一：双指针（错误）
        # 时间复杂度：
        # 空间复杂度：
        n = len(cards)
        
        left = 0
        min_length = float('inf')
        for right in range(1, n):
            while left < right:
                print(left, right)
                if cards[left] == cards[right]:
                    min_length = min(min_length, right - left + 1)
                left += 1
                    
        return min_length if min_length != float('inf') else -1
         
        
        # 方法二：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(cards)
        
        from collections import defaultdict, Counter     
        count = Counter(cards)
        #print(count)
        
        hash_table = defaultdict(list)
        for i, card in enumerate(cards):
            if count[card] > 1:
                hash_table[card].append(i)
        #print(hash_table)
        
        min_length = float('inf')
        for key, value in hash_table.items():
            length = len(value)
            for i in range(1, length):
                min_length = min(min_length, value[i] - value[i - 1] + 1)
                
        return min_length if min_length != float('inf') else -1
        
        
        
                
