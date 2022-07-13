"""
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。

压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题

"""

class Solution:
    def compress(self, chars: List[str]) -> int:


        # 方法一：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        #print(chars)
        n = len(chars)
        if n == 0 or n == 1:
            #print('n:', n)
            return 

        index = n - 2       
        tmp_char = chars[n-1]
        first_index = n - 1
        tmp_count = 1

        # 在原数组的基础上改为个数，并删除重复字母
        while index >= 0:
            #print(index)
            while index >= 0 and chars[index] == tmp_char:
                tmp_count += 1
                index -= 1
            
            if 1 < tmp_count < 10:
                #print('tmp_count:', tmp_count)
                chars[index + 2] = str(tmp_count)
                del chars[index + 3: first_index + 1]
            elif tmp_count >= 10:
                #print('tmp_count:', tmp_count)
                tmp_count_str = str(tmp_count)
                k = len(tmp_count_str)
                #print('k:', k)
                chars[index + 2: index + 2 + k] = tmp_count_str
                del chars[index + 2 + k: first_index + 1]

            #print(chars)

            if index >= 0:
                tmp_count = 0
                tmp_char = chars[index]
                first_index = index

        #print('chars:', chars)



        
