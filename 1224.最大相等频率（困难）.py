"""
给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：
从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。

如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。

示例 1：
输入：nums = [2,2,1,1,5,3,3,5]
输出：7
解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。

示例 2：
输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
输出：13
 
提示：
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

"""

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:


        # 方法一：双哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        from collections import Counter, defaultdict
        count = Counter(nums)

        times = defaultdict(set)
        for k, v in count.items():
            times[v].add(k)
        #print(times)

        for i in range(n - 1, -1, -1):
            #print('i:', i)
            if len(times[0]) == 0 or len(times[0]) > 0:
                del times[0]
            #print('count before:', count)
            #print('times before:', times)           
            if len(times) == 2:
                if len(times[1]) == 1:
                    return n - (n - i - 1)
                arr = []
                for k, v in times.items():
                    #print('k, v:', k, v)
                    if len(v) != 0:
                        arr.append(k)
                #print(arr)
                arr1, arr2 = max(arr), min(arr)
                #print(arr1, arr2)
                if arr1 - arr2 == 1 and len(times[arr1]) == 1:
                    return n - (n - i - 1)
            if len(times) == 1:
                if len(times[1]) > 0:
                    return n - (n - i - 1)
                if len(count) == 1:
                    return n - (n - i - 1)

            num = nums[i]
            time = count[num]
            times[time].discard(num)
            times[time - 1].add(num)
            count[num] -= 1

            if len(times[time]) == 0:
                del times[time]
            if len(times[1]) == 0:
                del times[1]
            if len(times[0]) == 0 or len(times[0]) > 0:
                del times[0]
            #print('count after:', count)
            #print('times after:', times) 

        return 0


        # 方法二：双哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        freq, count = Counter(), Counter()
        ans = maxFreq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
            freq[count[num]] += 1
            if maxFreq == 1 or \
               freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and freq[maxFreq] == 1 or \
               freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
        #print(count)
        #print(freq)
        return ans


            




