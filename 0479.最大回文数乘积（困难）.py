"""
给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。


示例 1:
输入：n = 2
输出：987
解释：99 x 91 = 9009, 9009 % 1337 = 987

示例 2:
输入： n = 1
输出： 9
 

提示:
1 <= n <= 8

"""

class Solution:
    def largestPalindrome(self, n: int) -> int:


        # 方法一：暴力法（超时）
        # 时间复杂度：O(10^2n)
        # 空间复杂度：O(1)
        if n == 1:
            return 9

        min_num, max_num = 10 ** (n - 1), 10 ** n - 1
        #print(min_num, max_num)
        
        ans = 0
        for num1 in range(max_num, min_num - 1, -1):
            num2 = num1
            while num2 >= min_num:
                tmp_num = num1 * num2
                tmp_length = len(str(tmp_num))
                #print(num1, num2, tmp_num)

                if tmp_length % 2 == 0:
                    if int(
                        str(tmp_num)[: (tmp_length + 1) // 2] \
                      + str(tmp_num)[: (tmp_length + 1) // 2][::-1] \
                    ) == tmp_num:                        
                        #print(num1, num2, tmp_num)
                        ans = max(ans, tmp_num)
                    num2 -= 1
                else:
                    if int(
                        str(tmp_num)[: (tmp_length + 1) // 2] \
                      + str(tmp_num)[: (tmp_length + 1) // 2 - 1][::-1] \
                    ) == tmp_num:                        
                        #print(num1, num2, tmp_num)
                        ans = max(ans, tmp_num)
                    num2 -= 1

        return ans % 1337


        # 方法二：枚举（超时）
        # 时间复杂度：O(10^2n)
        # 空间复杂度：O(1)
        if n == 1:
            return 9

        min_num, max_num = 10 ** (n - 1), 10 ** n - 1
        min_multi, max_multi = min_num ** 2, max_num ** 2
        #print(min_num, max_num)

        for num in range(max_multi, min_multi - 1, -1):           
            length = len(str(num))

            # 判断是否为回文数
            if length % 2 == 0:
                if int(
                        str(num)[: (length + 1) // 2] \
                      + str(num)[: (length + 1) // 2][::-1] \
                    ) != num:
                    continue
            else:
                if int(
                        str(num)[: (length + 1) // 2] \
                      + str(num)[: (length + 1) // 2 - 1][::-1] \
                    ) == num:
                    continue

            divisor = int(num ** 0.5)
            while divisor > 0:
                #print(num, divisor)
                remainder = num % divisor
                if remainder == 0 and len(str(divisor)) == n and len(str(num // divisor)) == n:
                    print(num, divisor)
                    return num % 1337
                else:
                    divisor -= 1


        # 方法三：枚举（超时）
        # 时间复杂度：O(10^2n)
        # 空间复杂度：O(1)
        def judge(num):
            divisor = int(num ** 0.5)
            #print('divisor:', divisor)
            while len(str(divisor)) >= n:
                #print('divisor:', divisor)
                if num % divisor == 0 and len(str(divisor)) == n and len(str(num // divisor)) == n:
                    print('True')
                    return True
                else:
                    divisor -= 1
            return False


        if n == 1:
            return 9
        #min_num, max_num = 10 ** (n - 1), 10 ** n - 1
        #min_multi, max_multi = min_num ** 2, max_num ** 2
        min_length = 2 * n - 1
        max_length = 2 * n

        for length in range(max_length, min_length - 1, -1):
            #print(length)
            max_num = 10 ** n - 1
            min_num = 10 ** (n - 1)
            num = max_num

            if length % 2 == 0:               
                while num >= min_num:                   
                    tmp_num = int(str(num) + str(num)[::-1])
                    #print('num, tmp_num:', num, tmp_num)
                    if judge(tmp_num):
                        return tmp_num % 1337
                    else:
                        num -= 1

            elif length % 2 != 0:
                while num >= min_num:
                    tmp_num = int(str(num) + str(num)[:-1][::-1])
                    #print('num, tmp_num:', num, tmp_num)
                    if judge(tmp_num):
                        return tmp_num
                    else:
                        num -= 1


        # 方法四：枚举
        # 时间复杂度：O(10^2n)
        # 空间复杂度：O(1)
        def judge(num, divisor):
            #print('divisor:', divisor)
            while divisor * divisor >= num:
                #print('divisor:', divisor)
                if num % divisor == 0:
                    print('True')
                    return True
                else:
                    divisor -= 1
            return False


        if n == 1:
            return 9
        #min_num, max_num = 10 ** (n - 1), 10 ** n - 1
        #min_multi, max_multi = min_num ** 2, max_num ** 2
        min_length = 2 * n - 1
        max_length = 2 * n

        for length in range(max_length, min_length - 1, -1):
            #print(length)
            max_num = 10 ** n - 1
            min_num = 10 ** (n - 1)
            num = max_num

            if length % 2 == 0:               
                while num >= min_num:                   
                    tmp_num = int(str(num) + str(num)[::-1])
                    #print('num, tmp_num:', num, tmp_num)
                    if judge(tmp_num, max_num):
                        return tmp_num % 1337
                    else:
                        num -= 1

            elif length % 2 != 0:
                while num >= min_num:
                    tmp_num = int(str(num) + str(num)[:-1][::-1])
                    #print('num, tmp_num:', num, tmp_num)
                    if judge(tmp_num, max_num):
                        return tmp_num % 1337
                    else:
                        num -= 1


                        











                        













