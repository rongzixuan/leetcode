"""
给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 
示例 1：
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]

示例 2：
输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
 
提示：
每棵树的节点数在 [0, 5000] 范围内
-10^5 <= Node.val <= 10^5

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:


        # 方法一：中序遍历 + 归并排序
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(m + n)
        # m和n分别为两棵树的节点数目
        nums1, nums2 = [], []

        def inOrder(root, nums):
            if not root:
                return 
            inOrder(root.left, nums)
            nums.append(root.val)
            inOrder(root.right, nums)

        inOrder(root1, nums1)
        inOrder(root2, nums2)

        ans = []
        i1, i2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i1 <= n1 and i2 <= n2:
            if i1 == n1:
                ans.extend(nums2[i2:])
                break
            if i2 == n2:
                ans.extend(nums1[i1:])
                break
            if nums1[i1] < nums2[i2]:
                ans.append(nums1[i1])
                i1 += 1
            else:
                ans.append(nums2[i2])
                i2 += 1

        return ans







