"""
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
注意：本题相对原题稍作修改

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == []:
            return []

        # 方法一：排序+哈希表
        hash_table = {}
        res = []

        index = 0
        for st in strs:
            st_out = "".join(sorted(st))
            if st_out not in hash_table:
                hash_table[st_out] = index
                index += 1
                res.append([st])
            else:
                res[hash_table[st_out]].append(st)

        #print(hash_table)
        #print(res)
        return res


        # 方法二：排序+哈希表
        res = defaultdict(list)

        for st in strs:
            st_out = "".join(sorted(st))
            res[st_out].append(st)

        return list(res.values())


        # 方法三：计数+哈希表
        res = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for ch in st:
                count[ord(ch) - ord('a')] += 1
            res[tuple(count)].append(st)

        return list(res.values())

