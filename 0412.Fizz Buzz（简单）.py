"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = []
        for i in range(n):
            flag3 = (((i+1) % 3) == 0)
            flag5 = (((i+1) % 5) == 0)
            #print(flag3, flag5)
            if flag3 and flag5:
                res.append('FizzBuzz')
            elif flag3:
                res.append('Fizz')
            elif flag5:
                res.append('Buzz')
            else:
                res.append(str(i+1))

        return res
    
    
    
    
