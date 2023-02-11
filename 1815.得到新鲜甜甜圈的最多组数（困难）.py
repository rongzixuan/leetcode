"""
有一个甜甜圈商店，每批次都烤 batchSize 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 所有 甜甜圈都必须已经全部销售完毕。给你一个整数 batchSize 和一个整数数组 groups ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 groups[i] 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。

当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。

你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多 有多少组人会感到开心。

示例 1：
输入：batchSize = 3, groups = [1,2,3,4,5,6]
输出：4
解释：你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。

示例 2：
输入：batchSize = 4, groups = [1,3,2,5,2,2,1,6]
输出：4
 
提示：
1 <= batchSize <= 9
1 <= groups.length <= 30
1 <= groups[i] <= 10^9

"""

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:


        # 方法一：记忆化搜索
        # 时间复杂度：
        # 空间复杂度：
        cnt = [0] * batchSize
        for x in groups:
            cnt[x % batchSize] += 1

        @cache  # 记忆化
        def dfs(left: int, cnt: Tuple[int]) -> int:
            #print('left, cnt:', left, cnt)
            res = 0
            cnt = list(cnt)
            for x, c in enumerate(cnt):  # 枚举顾客
                #print('x, c:', x, c)
                if c:  # cnt[x] > 0
                    cnt[x] -= 1
                    res = max(res, (left == 0) + dfs((left + x + 1) % batchSize, tuple(cnt)))  # x 从 0 开始，这里要 +1
                    cnt[x] += 1
            return res
        return cnt[0] + dfs(0, tuple(cnt[1:]))  # 转成 tuple 这样能记忆化






