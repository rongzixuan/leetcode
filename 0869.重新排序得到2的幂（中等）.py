"""
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

"""

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:


        # 方法一：回溯 + 位运算
        # 时间复杂度：O(length!)
        # 空间复杂度：O(length)
        n_array = list(str(n))
        #print(n_array)
        length = len(n_array)

        def backtrack(index):
            #print(n_array)
            if index == length:
                tmp_n = int(''.join(n_array))
                #print(tmp_n)
                if n_array[0] != '0' and (tmp_n & (tmp_n-1)) == 0:
                    #print('true')
                    return True
                else:
                    return 
            for i in range(length):
                #print(i, index)
                n_array[i], n_array[index] = n_array[index], n_array[i]
                if backtrack(index + 1):
                    return True
                n_array[i], n_array[index] = n_array[index], n_array[i]

        return True if backtrack(0) else False


        # 方法二：回溯 + 位运算 + 记忆化搜索
        # 时间复杂度：O(length!)
        # 空间复杂度：O(length)
        n_array = list(str(n))
        #print(n_array)
        length = len(n_array)
        visited = set()

        def backtrack(index):
            #print(n_array)                      
            if index == length:                
                #print(tmp_n)
                tmp_n = int(''.join(n_array))
                if n_array[0] != '0' and (tmp_n & (tmp_n-1)) == 0:
                    #print('true')
                    return True
                else:
                    return False
            for i in range(index, length):
                #print(i, index)
                n_array[i], n_array[index] = n_array[index], n_array[i]
                #print(visited)
                #print(''.join(n_array))
                if (i, index) not in visited:
                    #print('1')
                    visited.add((i, index))
                    if backtrack(index + 1):
                        #print(int(''.join(n_array)))
                        return True   
                    visited.remove((i, index))                                 
                n_array[i], n_array[index] = n_array[index], n_array[i]

        #print(visited)
        return True if backtrack(0) else False  


        # 方法三：预处理 + 哈希表
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        def getCount(n):
            tmp_count = [0] * 10
            while n:
                tmp_count[n % 10] += 1
                n //= 10
            return tuple(tmp_count)

        count = {getCount(1 << i) for i in range(30)}

        return getCount(n) in count

        
        

