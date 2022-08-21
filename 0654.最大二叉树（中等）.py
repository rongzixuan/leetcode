"""
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。

返回 nums 构建的 最大二叉树 。

示例 1：
输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]
解释：递归调用如下所示：
- [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。
        
示例 2：
输入：nums = [3,2,1]
输出：[3,null,2,null,1]

提示：
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
nums 中的所有整数 互不相同

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        # 方法一：递归
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        def dfs(node, left, right):
            #print(left, right)
            if left > right:
                return
            max_num = -1
            index = -1
            for i in range(left, right + 1):
                if nums[i] > max_num:
                    max_num = nums[i]
                    index = i
            node.val = max_num
            
            node.left = dfs(TreeNode(), left, index - 1)
            node.right = dfs(TreeNode(), index + 1, right)
            return node

        n = len(nums)
        root = TreeNode()
        return dfs(root, 0, n - 1)


        # 方法二：单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        stack = []
        left = [-1] * n    # 左边第一个比nums[i]大的数的索引
        right = [-1] * n   # 右边第一个比nums[i]大的数的索引
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop(-1)
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        #print('left:', left)   

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop(-1)
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        #print('right:', right)             

        root = None
        for i in range(n):
            if left[i] == right[i] == -1:
                root = tree[i]
            elif left[i] == -1:
                tree[right[i]].left = tree[i]
            elif right[i] == -1:
                tree[left[i]].right = tree[i]
            elif nums[left[i]] < nums[right[i]]:
                tree[left[i]].right = tree[i]
            else:
                tree[right[i]].left = tree[i]

        return root


        # 方法三：单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        stack = []
        left = [-1] * n    # 左边第一个比nums[i]大的数的索引
        right = [-1] * n   # 右边第一个比nums[i]大的数的索引
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stack and nums[stack[-1]] < nums[i]:
                right[stack[-1]] = i
                stack.pop(-1)
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        #print('left:', left)   
        #print('right:', right)             

        root = None
        for i in range(n):
            if left[i] == right[i] == -1:
                root = tree[i]
            elif left[i] == -1:
                tree[right[i]].left = tree[i]
            elif right[i] == -1:
                tree[left[i]].right = tree[i]
            elif nums[left[i]] < nums[right[i]]:
                tree[left[i]].right = tree[i]
            else:
                tree[right[i]].left = tree[i]

        return root


        # 方法四：单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        stack = []
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stack and nums[stack[-1]] < nums[i]:
                tree[i].left = tree[stack[-1]]
                stack.pop(-1)
            if stack:
                tree[stack[-1]].right = tree[i]
            stack.append(i)            

        return tree[stack[0]]





