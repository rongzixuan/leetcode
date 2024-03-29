"""
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

"""

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        # 方法一：数学
        # 时间复杂度：O(logn)
        # 空间复杂度：O(logn)
        res = []

        i = label
        while i >= 1:
            res.insert(0, i)
            i //= 2
        #print(res)

        n = len(res)
        for j in range(n-2, 0, -2):
            left, right = 2**j, 2**(j+1)-1
            #print(left, right)
            res[j] = right - (res[j] - left)
        #print(res)
        return res

    
    
    
    
