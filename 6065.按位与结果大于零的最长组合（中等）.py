"""
对数组 nums 执行 按位与 相当于对数组 nums 中的所有整数执行 按位与 。

例如，对 nums = [1, 5, 3] 来说，按位与等于 1 & 5 & 3 = 1 。
同样，对 nums = [7] 而言，按位与等于 7 。
给你一个正整数数组 candidates 。计算 candidates 中的数字每种组合下 按位与 的结果。 candidates 中的每个数字在每种组合中只能使用 一次 。

返回按位与结果大于 0 的 最长 组合的长度。


示例 1：
输入：candidates = [16,17,71,62,12,24,14]
输出：4
解释：组合 [16,17,62,24] 的按位与结果是 16 & 17 & 62 & 24 = 16 > 0 。
组合长度是 4 。
可以证明不存在按位与结果大于 0 且长度大于 4 的组合。
注意，符合长度最大的组合可能不止一种。
例如，组合 [62,12,24,14] 的按位与结果是 62 & 12 & 24 & 14 = 8 > 0 。

示例 2：
输入：candidates = [8,8]
输出：2
解释：最长组合是 [8,8] ，按位与结果 8 & 8 = 8 > 0 。
组合长度是 2 ，所以返回 2 。

提示：
1 <= candidates.length <= 10^5
1 <= candidates[i] <= 10^7

"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        
        # 方法一：位运算 + 哈希表
        # 时间复杂度：
        # 空间复杂度：
        n = len(candidates)
        count = defaultdict(int)
        
        for i, candidate in enumerate(candidates):
            bit = 1
            while candidate:
                if 1 & candidate:
                    count[bit] += 1
                bit += 1
                candidate >>= 1
        
        #print(count)
        return count[max(count, key=lambda x: count[x])]
        
        
        # 方法二：位运算
        # 时间复杂度：
        # 空间复杂度：
        return max(sum((num >> i) & 1 for num in candidates) for i in range(24))



        
