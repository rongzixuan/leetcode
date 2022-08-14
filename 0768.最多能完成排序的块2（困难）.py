"""
这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。
arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
我们最多能将数组分成多少块？

示例 1:
输入: arr = [5,4,3,2,1]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。 

示例 2:
输入: arr = [2,1,3,4,4]
输出: 4
解释:
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。 

注意:
arr的长度在[1, 2000]之间。
arr[i]的大小在[0, 10**8]之间。

"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:


        # 方法一：排序 + 哈希表
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        """
        用哈希表记录每个数字的坐标。
        从右到左依次找到最大元素所在的下标
        """
        """from collections import defaultdict
        #standard = ar.sort()
        standard = sorted(arr)
        n = len(arr)
        count = defaultdict(list)
        for i in range(n - 1, - 1, -1):
            count[arr[i]].append(i)
        #print(count)

        ans = 0
        left, right = n, n     # 上一个区间的左端、右端
        min_num = 10 ** 8 + 1   # 上一个区间的最小值
        for j in range(n - 1, -1, - 1):
            m = len(count[standard[j]])
            for k in range(m):
                if count[standard[j]][k] < left:
                    if standard[j] <= min_num:
                        ans += 1
                        right = left
                        left = count[standard[j]][k]                                      
                    else:
                        left = count[standard[j]][k]
                    min_num = min(arr[index] for index in range(left, right)) 
                    #print('min_num:', min_num)
        return ans"""


        # 方法二：排序 + 哈希表
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        """cnt = Counter()
        res = 0
        for x, y in zip(arr, sorted(arr)):
            cnt[x] += 1
            if cnt[x] == 0:
                del cnt[x]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            if len(cnt) == 0:
                res += 1
        return res"""


        # 方法三：单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        stack = []
        for num in arr:
            if len(stack) == 0 or num >= stack[-1]:
                stack.append(num)
            else:
                mx = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(mx)
        return len(stack)





