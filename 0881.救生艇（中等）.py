"""
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:


        # 方法一：贪心
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        count = 0
        n = len(people)
        if n == 1:
            return 1

        people.sort()
        left, right = 0, n-1
        while people[right] == limit:
            count += 1
            right -= 1
        while left <= right:
            if people[left] + people[right] <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count += 1
                right -= 1

        return count

        


