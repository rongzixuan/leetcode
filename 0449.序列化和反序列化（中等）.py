"""
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
编码的字符串应尽可能紧凑。
 
示例 1：
输入：root = [2,1,3]
输出：[2,1,3]

示例 2：
输入：root = []
输出：[]

提示：
树中节点数范围是 [0, 10^4]
0 <= Node.val <= 10^4
题目数据 保证 输入的树是一棵二叉搜索树。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一：后序遍历
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []

        def postOrder(node):
            if not node:
                return 
            postOrder(node.left)
            postOrder(node.right)
            arr.append(node.val)

        postOrder(root)
        #print(arr)
        #print(' '.join(map(str, arr)))
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = list(map(int, data.split()))
        #print(arr)

        def getNum(left, right):
            if not arr or arr[-1] < left or arr[-1] > right:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = getNum(val, right)
            root.left = getNum(left, val)
            return root

        return getNum(-inf, inf)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
