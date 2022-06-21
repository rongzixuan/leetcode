"""
将非负整数 num 转换为其对应的英文表示。

"""

class Solution:
    def numberToWords(self, num: int) -> str:


        # 方法一：递归
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        if num == 0:
            return "Zero"

        res = ""
        singles = ['One', 'Two', 'Three', 'Four', 'Five', 
                   'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        tenplus = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 
                   'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 
                'Sixty', 'Seventy', 'Eighty', 'Ninety']
        units = ['Hundred', 'Thousand', 'Million', 'Billion']
        
        #n = len(str(num))

        def recursion(num):
            #print(num)
            s = ""
            if num == 0:
                return s
            elif num <= 10:
                s += singles[num - 1] + " "
            elif num < 20:
                s += tenplus[num - 11] + " "
            elif num < 100:
                s += tens[num // 10 - 2] + " "
                #s += singles[num % 10 - 1] + " " 
                s += recursion(num % 10)
            else:
                s += singles[num // 100 - 1] + " "
                s += units[0] + " "
                s += recursion(num % 100) 
            return s


        #res += singles[num // 10**9 - 1]
        #res += units[3]
        s0 = recursion(num // 10**9)
        if s0:
            #print('s0:', s0)
            res += s0 + units[3] + " "
        s1 = recursion(num // 10**6 - num // 10**9 * 1000)
        if s1:
            #print('s1:', s1)
            res += s1 + units[2] + " "
        s2 = recursion(num // 10**3 - num // 10**6 * 1000)
        if s2:
            #print('s2:', s2)
            res += s2 + units[1] + " "
        s3 = recursion(num % 10**3)
        if s3:
            #print('s3:', s3)
            res += s3

        return res.strip()


        # 方法二：迭代
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        if num == 0:
            return "Zero"

        res = ""
        singles = ['One', 'Two', 'Three', 'Four', 'Five', 
                   'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        tenplus = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 
                   'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 
                'Sixty', 'Seventy', 'Eighty', 'Ninety']
        units = ['Hundred', 'Thousand', 'Million', 'Billion']
        
        #n = len(str(num))

        def recursion(num):
            #print(num)
            s = ""
            if num == 0:
                return s
            if num >= 100:
                s += singles[num // 100 - 1] + " "
                s += units[0] + " "
                num %= 100
            if num >= 20:
                s += tens[num // 10 - 2] + " "
                num %= 10             
            if num > 10:
                s += tenplus[num - 11] + " "  
            if 10 >= num > 0:
                s += singles[num - 1] + " "
                      
            return s

        s0 = recursion(num // 10**9)
        if s0:
            #print('s0:', s0)
            res += s0 + units[3] + " "
        s1 = recursion(num // 10**6 - num // 10**9 * 1000)
        if s1:
            #print('s1:', s1)
            res += s1 + units[2] + " "
        s2 = recursion(num // 10**3 - num // 10**6 * 1000)
        if s2:
            #print('s2:', s2)
            res += s2 + units[1] + " "
        s3 = recursion(num % 10**3)
        if s3:
            #print('s3:', s3)
            res += s3

        return res.strip()
            

