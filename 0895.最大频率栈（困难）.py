"""
设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。

实现 FreqStack 类:
FreqStack() 构造一个空的堆栈。
void push(int val) 将一个整数 val 压入栈顶。
int pop() 删除并返回堆栈中出现频率最高的元素。

如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。
 

示例 1：

输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]

输出：[null,null,null,null,null,null,null,5,7,5,4]

解释：
FreqStack = new FreqStack();
freqStack.push (5);//堆栈为 [5]
freqStack.push (7);//堆栈是 [5,7]
freqStack.push (5);//堆栈是 [5,7,5]
freqStack.push (7);//堆栈是 [5,7,5,7]
freqStack.push (4);//堆栈是 [5,7,5,7,4]
freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
 

提示：
0 <= val <= 10^9
push 和 pop 的操作数不大于 2 * 10^4。
输入保证在调用 pop 之前堆栈中至少有一个元素。

"""

# 方法一：哈希表 + 优先队列（最小堆）
# 时间复杂度：
# 空间复杂度：
from collections import defaultdict
import heapq as hp
class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.queue = []
        self.index = 1

    def push(self, val: int) -> None:  
        self.count[val] += 1
        hp.heappush(self.queue, (-self.count[val], -self.index, val))
        self.index += 1
        #print('val:', val)
        #print('self.count:', self.count)
        #print('self.queue:', self.queue)

    def pop(self) -> int:
        val = hp.heappop(self.queue)[2]
        #print(val)
        self.count[val] -= 1
        #print('val:', val)
        #print('self.count:', self.count)
        #print('self.queue:', self.queue)
        return val


# 方法二：双哈希表
# 时间复杂度：
# 空间复杂度：
from collections import defaultdict
import heapq as hp
class FreqStack:

    def __init__(self):
        self.count1 = defaultdict(int)
        self.count2 = defaultdict(list)
        self.max_num = 0

    def push(self, val: int) -> None:  
        self.count1[val] += 1
        self.count2[self.count1[val]].append(val)
        if self.count1[val] > self.max_num:
            self.max_num = self.count1[val]
        #print('self.count1:', self.count1)
        #print('self.count2:', self.count2)
        #print('push val:', val)

    def pop(self) -> int:       
        val = self.count2[self.max_num].pop()
        if len(self.count2[self.max_num]) == 0:
            self.max_num -= 1
        self.count1[val] -= 1
        #print('self.count1:', self.count1)
        #print('self.count2:', self.count2)
        #print('pop val:', val)
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


