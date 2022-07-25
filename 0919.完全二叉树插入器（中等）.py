"""
完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。
设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 CBTInserter 类:
CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
CBTInserter.get_root() 将返回树的头节点。
 
示例 1：

输入
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
输出
[null, 1, 2, [1, 2, 3, 4]]

解释
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // 返回 1
cBTInserter.insert(4);  // 返回 2
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
 
提示：
树中节点数量范围为 [1, 1000] 
0 <= Node.val <= 5000
root 是完全二叉树
0 <= val <= 5000 
每个测试用例最多调用 insert 和 get_root 操作 10^4 次

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一：广度优先搜索 + 队列
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.candidate = deque()

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not node.left or not node.right:
                self.candidate.append(node)

    def insert(self, val: int) -> int:
        node = self.candidate[0]
        if not node.left:
            node.left = TreeNode(val)
            self.candidate.append(node.left)
        else:
            node.right = TreeNode(val)
            self.candidate.append(node.right)
            self.candidate.popleft()
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# 方法二：广度优先搜索 + 位运算
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.count = 0

        queue = deque([root])
        while queue:
            node = queue.popleft()
            self.count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)                

    def insert(self, val: int) -> int:
       # print('val:', val)
        self.count += 1
        self.node = self.root
        length = self.count.bit_length() - 1

        for i in range(length - 1, 0, -1):
            #print('i:', i)
            #print('self.count & (1 << i):', self.count & (1 << i))
            if self.count & (1 << i):
                self.node = self.node.right
            else:
                self.node = self.node.left

        if self.count & 1:
            self.node.right = TreeNode(val)
        else:
            self.node.left = TreeNode(val)
        return self.node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

