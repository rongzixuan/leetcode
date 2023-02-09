"""
你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。

如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。

文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。

例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。
 
示例 1：
输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。

示例 2：
输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d" 都会被删除，因为它们都是 "/a" 的子文件夹。

示例 3：
输入: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
输出: ["/a/b/c","/a/b/ca","/a/b/d"]

提示：
1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] 只包含小写字母和 '/'
folder[i] 总是以字符 '/' 起始
每个文件夹名都是 唯一 的

"""

from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.end = False

    def insert(self, arr):
        node = self
        res = True
        #print('arr:', arr)
        for ch in arr:
            node = node.children[ch]
            if node.end == True:
                res = False
        node.end = True
        return res

class Trie:
    def __init__(self):
        self.children = {}
        self.fid = -1

    def insert(self, i, f):
        node = self
        ps = f.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = Trie()
            node = node.children[p]
        node.fid = i

    def search(self):
        def dfs(root):
            if root.fid != -1:
                ans.append(root.fid)
                return
            for child in root.children.values():
                dfs(child)

        ans = []
        dfs(self)
        return ans


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:


        # 方法一：排序 + 模拟
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        n = len(folder)       
        folder.sort()
        #print(folder)

        ans = [folder[0]]
        for i in range(1, n):
            m1, m2 = len(ans[-1]), len(folder[i])
            if m2 <= m1:
                ans.append(folder[i])
            else:
                if folder[i][0: m1] != ans[-1] or folder[i][m1] != '/':
                    ans.append(folder[i])
        return ans


        # 方法二：排序 + 字典树
        # 时间复杂度：O(n*logn + n * m)
        # 空间复杂度：O(1)
        # m为f平均长度
        folder.sort()
        trie = Trie()
        ans = []
        for f in folder:
            arr = f.split('/')
            flag = trie.insert(arr)
            if flag == True:
                ans.append(f)
        return ans


        # 方法三：字典树
        # 时间复杂度：O(n * m)
        # 空间复杂度：O(1)
        # m为f平均长度
        trie = Trie()
        for i, f in enumerate(folder):
            trie.insert(i, f)
        return [folder[i] for i in trie.search()]
             



