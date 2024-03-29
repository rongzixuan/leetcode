"""
给你两个整数数组 persons 和 times 。在选举中，第 i 张票是在时刻为 times[i] 时投给候选人 persons[i] 的。

对于发生在时刻 t 的每个查询，需要找出在 t 时刻在选举中领先的候选人的编号。

在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

实现 TopVotedCandidate 类：
TopVotedCandidate(int[] persons, int[] times) 使用 persons 和 times 数组初始化对象。
int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。
 
示例：
输入：
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
输出：
[null, 0, 1, 1, 0, 0, 1]

解释：
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
topVotedCandidate.q(15); // 返回 0
topVotedCandidate.q(24); // 返回 0
topVotedCandidate.q(8); // 返回 1
 
提示：
1 <= persons.length <= 5000
times.length == persons.length
0 <= persons[i] < persons.length
0 <= times[i] <= 10^9
times 是一个严格递增的有序数组
times[0] <= t <= 10^9
每个测试用例最多调用 10^4 次 q

"""


# 方法一：二分查找
# 时间复杂度：
# __init__()：O(n)
# q()：O(m * logn)
# 空间复杂度：O(n)
# 其中，n为数组persons和times的长度，m为查询的长度
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

        #self.count = [[0] * len(persons) for _ in range(len(persons))]
        #self.last = [[-1] * len(persons) for _ in range(len(persons))]
        last = [0] * len(persons)
        self.tops = [0] * len(persons)
        count_num = [0] * len(persons)
        top = -1       
        for i, person in enumerate(persons):
            count_num[person] += 1
            if count_num[person] >= count_num[top]:
                top = person
            self.tops[i] = top
        #print('self.last:', self.last)
        #print('self.count:', self.count)
        #print('self.tops:', self.tops)

    def q(self, t: int) -> int:
        n = len(self.times)
        #print('t:', t)

        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            #print(left, right, mid)
            if self.times[mid] == t:
                right = mid
                break
            elif self.times[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        #print('right:', right)
        return self.tops[right]

        """max_num = max(self.count[right])
        max_count = set()
        for k, v in enumerate(self.count[right]):
            if v == max_num:
                max_count.add(k)
        #print('max_count:', max_count)
        if len(max_count) > 1 :
            last = 0
            res = -1
            for mc in max_count:
                #print(self.persons[i])
                if self.last[right][mc] > last:
                    last = self.last[right][mc]
                    res = mc
            #print('res:', res)
            return res
        else:
            for num in max_count:
                #print(num)
                return num"""


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
