"""
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。

例如，数字字符串 "3322251" 的描述如下图：

"""

class Solution:
    def countAndSay(self, n: int) -> str:


        # 方法一：模拟
        # 时间复杂度：O(n * L)， 其中L味字符串最长长度
        # 空间复杂度：O(1)
        res = "1"
        if n == 1:
            return res

        for i in range(1, n):
            tmp_res = res
            res = ""
            #print('tmp_res:', tmp_res)
            length = len(tmp_res)
            #print('length:', length)

            if length == 1:
                res = '1' + tmp_res[0]
            else:
                count = 1
                j = 1
                while j < length:
                    #print('j:', j)
                    if tmp_res[j] == tmp_res[j-1]:
                        count += 1 
                        if j == length - 1:
                            res += str(count) + tmp_res[j]                  
                    else:
                        res += str(count) + tmp_res[j-1]
                        if j == length - 1:
                            res += "1" + tmp_res[j] 
                        count = 1
                    j += 1


            #print('res:', res)

        return res


        # 方法二：模拟 + 双指针
        # 时间复杂度：O(n * L)， 其中L味字符串最长长度
        # 空间复杂度：O(1)
        res = "1"
        if n == 1:
            return res

        for i in range(1, n):
            tmp_res = res
            res = ""
            length = len(tmp_res)
            count = 0

            j = k = 0
            while k < length:
                while k < length and tmp_res[j] == tmp_res[k]:
                    count += 1
                    k += 1
                res += str(count) + tmp_res[j]
                count = 0
                j = k

        return res

        
       
