"""
我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。

注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。

示例 1：
输入： stickers = ["with","example","science"], target = "thehat"
输出：3
解释：
我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。

示例 2:
输入：stickers = ["notice","possible"], target = "basicbasic"
输出：-1
解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。

提示:
n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target.length <= 15
stickers[i] 和 target 由小写英文单词组成

"""

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:


        # 方法一：广度优先搜索（超时）
        # 时间复杂度：
        # 空间复杂度：
        tmp_stickers = []
        for i, sticker in enumerate(stickers):
            if  not set(sticker).isdisjoint(set(target)):
                tmp_stickers.append(sticker)
        #print(len(stickers), len(tmp_stickers))
        #print(tmp_stickers)

        from collections import defaultdict, Counter 
        #count1 = []  
        count11 = defaultdict(int)  
        for i, sticker in enumerate(tmp_stickers):
            #tmp_count = defaultdict(int)
            for ch in sticker:
                #tmp_count[ch] += 1
                count11[ch] += 1
            #count1.append(tmp_count)          
        #print(count1)
        #print(count11)
        
        count2 = Counter(target)
        count22 = [0] * 26
        #print(count2)
        for k, v in count2.items():
            count22[ord(k) - ord('a')] += v
            if k not in count11:
                return -1
        #print('count22:', count22)

        ans = 0
        n = len(tmp_stickers)
        queue = deque([])
        for i in range(n):
            tmp = [0] * n
            tmp[i] = 1
            tmp_count = count22.copy()
            for ch in tmp_stickers[i]:
                tmp_count[ord(ch) - ord('a')] -= 1
            queue.append((tmp, tmp_count,  1))
        #print('queue:', queue)

        m = len(target)
        visited = set()
        while queue:
            nums, count, time = queue.popleft() 
            if time > m:
                return -1
            #print('nums, count, time, sum(count):', nums, count, time, sum(count))                  
            for i in range(n):
                tmp_nums = nums.copy()
                tmp_count = count.copy()              
                tmp_nums[i] += 1
                for ch in tmp_stickers[i]:
                    tmp_count[ord(ch) - ord('a')] -= 1
                #print('tmp_count, sum(count):', tmp_count, sum(tmp_count))
                if all([v <= 0 for k, v in enumerate(tmp_count)]):
                    return time + 1 
                if tuple(tmp_nums) not in visited:              
                    queue.append((tmp_nums, tmp_count, time + 1))
                    visited.add(tuple(tmp_nums))


        # 方法二：哈希表 + 广度优先搜索
        # 时间复杂度：
        # 空间复杂度：
        def trans(s):
            cnts = Counter()
            for c in s:
                if c in target:
                    cnts[c] += 1
            return cnts

        availables = [c for st in stickers if (c:=trans(st))]
        #print(availables)
        queue = deque([(target, 0)])
        explored = {target}
        while queue:
            cur, step = queue.popleft()
            #print('cur, step:', cur, step)
            if not cur:
                return step
            for avl in availables:
                #print('avl:', avl)
                if cur[0] in avl:
                    nxt = cur
                    for k, v in avl.items():
                        nxt = nxt.replace(k, '', v)
                        #print('nxt:', nxt)
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append((nxt, step + 1))
        return -1


        # 方法三：记忆化搜索 + 动态规划
        # 时间复杂度：
        # 空间复杂度：
        m = len(target)
        @cache
        def dp(mask: int) -> int:
            if mask == 0:
                return 0
            res = m + 1
            for sticker in stickers:
                left = mask
                cnt = Counter(sticker)
                for i, c in enumerate(target):
                    if mask >> i & 1 and cnt[c]:
                        cnt[c] -= 1
                        left ^= 1 << i
                if left < mask:
                    res = min(res, dp(left) + 1)
            return res
        res = dp((1 << m) - 1)
        return res if res <= m else -1


      
