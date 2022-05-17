"""
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。


示例 1：
输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。

示例 2：
输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。

示例 3：
输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。

提示：
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
在 words[i] 和 order 中的所有字符都是英文小写字母。

"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:


        # 方法一：遍历
        # 时间复杂度：O(n * m)
        # 空间复杂度：O(C)
        # n = len(words)
        # m = max(len(word))
        # C = 26
        n = len(words)
        if n == 1:
            return True

        order_dict = {v: k for k, v in enumerate(order)}
        #print(order_dict)

        for i in range(1, n):
            pre, cur = words[i - 1], words[i]
            n1, n2 = len(pre), len(cur)
            min_n = min(n1, n2)
            if pre[:min_n] == cur[:min_n] and n1 > n2:
                return False

            for j in range(min_n):
                if order_dict[pre[j]] > order_dict[cur[j]]:
                    return False
                elif order_dict[pre[j]] < order_dict[cur[j]]:
                    break
                elif order_dict[pre[j]] == order_dict[cur[j]]:
                    continue

        return True


        # 方法二：遍历
        # 时间复杂度：O(n * m)
        # 空间复杂度：O(C)
        # n = len(words)
        # m = max(len(word))
        # C = 26
        index = {c: i for i, c in enumerate(order)}
        return all(s <= t for s, t in pairwise([index[c] for c in word] for word in words))




