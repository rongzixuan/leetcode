"""
Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。

给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。

示例 1：
输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：true
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。

示例 2：
输入：hand = [1,2,3,4,5], groupSize = 4
输出：false
解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。
 
提示：
1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length

"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        # 方法一：排序 + 哈希表
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()

        from collections import defaultdict
        hash_table = defaultdict(int)
        for ch in hand:
            hash_table[ch] += 1
        #print(hash_table)

        while n:
            #print('hash_table:', hash_table)
            for k in list(hash_table.keys()):
                #print('hash_table2:', hash_table)
                #print('n, k, v:', n, k, hash_table[k])
                if (k - 1 not in hash_table or hash_table[k - 1] == 0) and hash_table[k] != 0:
                    for i in range(groupSize):
                        #print('k + i:', k + i)
                        hash_table[k + i] -= 1
                        n -= 1
                        if hash_table[k + i] < 0:
                            #print('false k + i:', k + i)
                            return False

        return True


        # 方法二：排序 + 哈希表
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        from collections import Counter
        cnt = Counter(hand)

        for ch in hand:
            if cnt[ch] == 0:
                continue
            for i in range(ch, ch + groupSize):
                cnt[i] -= 1
                if cnt[i] < 0:
                    return False

        return True


        # 方法三：哈希表 + 优先队列（堆）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(hand)
        if n % groupSize != 0:
            return False

        #hand.sort()
        from collections import defaultdict
        hash_table = defaultdict(int)

        import heapq
        heap = []
        for ch in hand:
            hash_table[ch] += 1
            heapq.heappush(heap, ch)
        #print('heap:', heap)
        #print('hash_table:', hash_table)

        while heap:
            k = heapq.heappop(heap)
            #print('k:', k)
            if hash_table[k] == 0:
                continue
            for i in range(k, k + groupSize):
                if i not in hash_table:
                    #print('false1:', i)
                    return False
                hash_table[i] -= 1
                if hash_table[i] < 0:
                    #print('false2:', i)
                    return False

        return True




