"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

"""

class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]

        # 方法一：位运算1-Brian Kernighan 算法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        res = []
        for i in range(n+1):
            j = i
            count = 0
            while j > 0:
                count += 1
                j &= j-1
            res.append(count)

        return res


        # 方法二：奇偶性1
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        res = [0] * (n+1)

        for i in range(1, n+1):
            #print('i:', i)
            if i % 2 == 1: # 奇数
                #print('i-1:', i)
                res[i] = res[i-1] + 1
                #print(res)

            elif i % 2 == 0: # 偶数
                #print('i-2:', i)
                i_tmp = i
                while i_tmp % 2 == 0 and i_tmp > 0:
                    #print(i)
                    i_tmp /= 2

                if i_tmp % 2 == 0: # 2的幂
                    res[i] = 1
                    #print('i-3:', i)
                elif i_tmp % 2 ==1:
                    #print('i-4:', i)
                    j = i
                    count = 0
                    while j > 0:
                        count += 1
                        j &= j-1
                    res[i] = count
        
        return res


        # 方法三：奇偶性2
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = [0] * (n+1)

        for i in range(1, n+1):
            if i % 2 == 1: # 奇数
                res[i] = res[i-1] + 1
            elif i % 2 == 0: # 偶数
                res[i] = res[i//2]

        return res


        # 方法四：动态规划-最高有效位
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = [0]

        high_bite = 0
        for i in range(1, n+1):
            if i & (i-1) == 0:  # 2的幂
                high_bite = i
                res.append(1)
            else:
                res.append(res[i-high_bite] + 1)

        return res


        # 方法五：动态规划-最低有效位
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = [0]

        for i in range(1, n+1):
            #print(i)
            res.append(res[i >> 1] + (i & 1))

        return res


        # 方法六：动态规划-最低设置位
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = [0]

        for i in range(1, n+1):
            res.append(res[i & (i-1)] + 1)

        return res


