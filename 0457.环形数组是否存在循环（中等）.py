"""
存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：

如果 nums[i] 是正数，向前 移动 nums[i] 步
如果 nums[i] 是负数，向后 移动 nums[i] 步
因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。

数组中的 循环 由长度为 k 的下标序列 seq ：

遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
所有 nums[seq[j]] 应当不是 全正 就是 全负
k > 1
如果 nums 中存在循环，返回 true ；否则，返回 false 。

"""

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:


        # 方法一：模拟法
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 0 or n == 1:
            return False

        for i in range(n):

            j = i
            distance = 0
            count = 0
            direction = 1 if nums[i] > 0 else -1

            while count <= n:
                #print('i:', i)
                #print('j:', j)
                tmp_direction = 1 if nums[j] > 0 else -1
                if tmp_direction != direction:
                    break
               
                #distance += abs(nums[j])               
                
                if j == i and count != 0:
                #if distance % n == 0 and count > 1:                   
                    if count > 1:  
                        #print('True:', i)    
                        #print('count:', count)                 
                        return True
                    else:
                        #print('False:', i) 
                        #print('count:', count)  
                        break

                count += 1
                j += nums[j]
                if j >= n:
                    j = j % n
                elif j < 0:
                    j = n -abs(j) % n

        return False



        # 方法二：模拟法-使用标记
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        if n == 0 or n == 1:
            return False
        mark = [-1] * n

        for i in range(n):
            if mark[i] != -1:
                continue
            j = i
            count = 0
            direction = 1 if nums[i] > 0 else -1

            while count <= n:
                #print(i, j)
                tmp_direction = 1 if nums[j] > 0 else -1
                if tmp_direction != direction:
                    #print('3:', i, j)
                    break

                if mark[j] != -1:
                    if mark[j] != i:
                        #print('2:', i, j)
                        break
                    elif mark[j] == i:
                        return True

                mark[j] = i    
                #print('mark:', mark)           
                
                count += 1
                next_j = j + nums[j]
                if next_j >= n:
                    next_j = next_j % n
                elif next_j < 0:
                    next_j = n - abs(next_j) % n
                #print('j, next_j:', j, next_j)

                if next_j == j:
                # $print('1:', i, j)
                    break
                else:
                    j = next_j

        return False



        # 方法三：双指针（快慢指针）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)

        def getNext(i):
            return (i + nums[i] + n) % n

        for i in range(n):
            fast, slow = getNext(i), i

            while nums[i] * nums[fast] > 0 and nums[i] * nums[getNext(fast)] > 0: # 方向相同
                if slow == fast:
                    if slow == getNext(slow):
                        break
                    else:
                        return True
                
                slow = getNext(slow)
                fast = getNext(getNext(fast))

        return False






         


         
