"""
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
返回所有可能的结果。答案可以按 任意顺序 返回。

"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:


        # 方法一：回溯+剪枝
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n^2)
        res = []
        lremove, rremove = 0, 0
        for ch in s:
            if ch == '(':
                lremove += 1
            elif ch == ')':
                if lremove > 0:
                    lremove -= 1
                else:
                    rremove += 1

        def check(s_):
            count = 0
            for ch in s_:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                if count < 0:
                    return 
            return count == 0

        def helper(s, start, lcount, rcount, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if check(s):
                    res.append(s)
            for i in range(start, len(s)):
                if i > start and s[i] == s[i-1]:
                    continue
                if lremove + rremove > len(s) - i:
                    break
                if s[i] =='(' and lremove > 0:
                    helper(s[:i] + s[i+1:], i, lcount, rcount, lremove-1, rremove)
                if s[i] == ')' and rremove > 0:
                    helper(s[:i] + s[i+1:], i, lcount, rcount, lremove, rremove-1)

        helper(s, 0, 0, 0, lremove, rremove)
        return res


        # 方法二：广度优先搜索
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O()       
        def check(s_):
            count = 0
            for ch in s_:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    return 
            return count == 0

        res = []
        hash_set = set([s])
        while True:
            for tmp_s in hash_set:
                #print(tmp_s)
                if check(tmp_s):                   
                    res.append(tmp_s)
            if len(res) > 0:
                return res
            new_hash_set = set()
            for tmp_s in hash_set:
                for i in range(len(tmp_s)):
                    if i > 0 and tmp_s[i] == s[i-1]:
                        continue
                    if tmp_s[i] == '(' or tmp_s[i] == ')':
                        new_hash_set.add(tmp_s[:i] + tmp_s[i+1:])
            hash_set = new_hash_set

        return res 


