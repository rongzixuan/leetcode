"""
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
 
示例 1：
输入: root = [5,3,6,2,4,null,7], k = 9
输出: true

示例 2：
输入: root = [5,3,6,2,4,null,7], k = 28
输出: false

提示:
二叉树的节点个数的范围是  [1, 10^4].
-10^4 <= Node.val <= 10^4
root 为二叉搜索树
-10^5 <= k <= 10^5

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:


        # 方法一：深度优先搜索（递归） + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        from collections import defaultdict
        count = defaultdict(int)

        def dfs(node):
            if not node:
                return False

            nonlocal count
            if k - node.val in count:
                #print(node.val, k - node.val)
                return True
            count[node.val] += 1
            res1 = dfs(node.left)
            res2 = dfs(node.right)
            return True if (res1 or res2) else False

        #print(count)
        return True if dfs(root) else False


        # 方法二：深度优先搜索（栈） + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        stack = [root]
        from collections import defaultdict
        count = defaultdict(int)

        while stack:
            node = stack.pop()
            if k - node.val in count:
                #print(node.val, k - node.val)
                return True
            count[node.val] += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False


        # 方法三：广度优先搜索 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        queue = [root]
        from collections import defaultdict
        count = defaultdict(int)

        while queue:
            node = queue.pop(0)
            if k - node.val in count:
                #print(node.val, k - node.val)
                return True
            count[node.val] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False


        # 方法四：中序遍历（递归） + 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        arr = []
        
        def midOrder(node):
            if not node:
                return 
            midOrder(node.left)
            arr.append(node.val)
            midOrder(node.right)
        midOrder(root)

        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] == k:
                return True
            elif arr[left] + arr[right] < k:
                left += 1
            else:
                right -= 1

        return False


        # 方法五：中序遍历（迭代-栈） + 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        left, right = root, root
        left_stack, right_stack = [root], [root]

        while left.left:
            left_stack.append(left.left)
            left = left.left

        while right.right:
            right_stack.append(right.right)
            right = right.right

        while left !=  right:
            if left.val + right.val == k:
                return True
            elif left.val + right.val < k:
                left = left_stack.pop()
                node = left.right
                while node:
                    left_stack.append(node)
                    node = node.left
            else:
                right = right_stack.pop()
                node = right.left
                while node:
                    right_stack.append(node)
                    node = node.right

        return False



