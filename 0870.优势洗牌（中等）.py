"""
给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。
返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。

示例 1：
输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
输出：[2,11,7,15]

示例 2：
输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
输出：[24,32,8,12]
 
提示：
1 <= nums1.length <= 10^5
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 10^9

"""

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:


        # 方法一：排序 + 贪心 + 双指针 + 哈希表
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(nums1)
        from collections import defaultdict
        hash_table = {i:-1 for i in range(n)}
        #print(hash_table)
        #hash_table = {}
        tmp_nums1 = [(num, i) for i, num in enumerate(nums1)]
        tmp_nums1.sort()
        tmp_nums2 = [(num, i) for i, num in enumerate(nums2)]
        tmp_nums2.sort()
        used = [False] * n
        #print(tmp_nums1, tmp_nums2)

        i = 0
        end_flag = False
        for j in range(n):
            #print(i, j)
            if not end_flag:
                while i < n and tmp_nums1[i][0] <= tmp_nums2[j][0]:
                    i += 1
                if i < n:
                    hash_table[tmp_nums2[j][1]] = tmp_nums1[i][1]
                    used[i] = True
                    i = i + 1
                if i == n:
                    end_flag = True
                    i = 0
            if hash_table[tmp_nums2[j][1]] == -1:
                while i < n and used[i] == True:
                    i += 1
                if i < n:
                    hash_table[tmp_nums2[j][1]] = tmp_nums1[i][1]
                    used[i] = True
                    i += 1
            #print(hash_table)

        #print(hash_table)
        ans = []
        for i, num in enumerate(nums2):
            ans.append(nums1[hash_table[i]])
        return ans


        # 方法二：排序 + 贪心 + 双指针
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(nums1)
        idx1, idx2 = list(range(n)), list(range(n))
        idx1.sort(key=lambda x: nums1[x])
        idx2.sort(key=lambda x: nums2[x])

        ans = [0] * n
        left, right = 0, n - 1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ans[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ans[idx2[right]] = nums1[idx1[i]]
                right -= 1
        
        return ans



