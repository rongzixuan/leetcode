"""
在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。

如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
否则，x 将会向 y 发送一条好友请求。

注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。

返回在该社交媒体网站上产生的好友请求总数。

 
示例 1：
输入：ages = [16,16]
输出：2
解释：2 人互发好友请求。

示例 2：
输入：ages = [16,17,18]
输出：2
解释：产生的好友请求为 17 -> 16 ，18 -> 17 。

示例 3：
输入：ages = [20,30,100,110,120]
输出：3
解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。
 

提示：
n == ages.length
1 <= n <= 2 * 10^4
1 <= ages[i] <= 120

"""

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:


        # 方法一：排序 + 双指针
        # 时间复杂度：O(nlogn + n)
        # 空间复杂度：O(1)
        n = len(ages)
        if n == 1:
            return 0

        res = 0
        ages.sort(reverse=True)
        #print(ages)
        left, right = 0, 0
        for i in range(n):
            while ages[left] > ages[i]:
                left += 1
            while right < n and ages[right] > 0.5 * ages[i] + 7:
                right += 1
            #print(i, left, right)
            res += max(0, right - left - 1)

        return res


        # 方法二：计数排序 + 前缀和
        # 时间复杂度：O(n + C)
        # 空间复杂度：O(C)
        # C = 120
        n = len(ages)
        if n == 1:
            return 0

        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        pre_sum = []
        tmp_sum = 0
        for c in cnt:
            tmp_sum += c
            pre_sum.append(tmp_sum)
        #print(cnt)
        #print(pre_sum)

        res = 0
        for age in ages:
            res += max(0, pre_sum[age] - pre_sum[int(0.5 * age + 7)] - 1)
            #print(age, res)

        return res


    
    
