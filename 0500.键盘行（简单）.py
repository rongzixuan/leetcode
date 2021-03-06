"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：
第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        # 方法一：遍历
        # 时间复杂度：O(L)，L为所有单词的总长度
        # 空间复杂度：O(1)
        #set1 = {'q','w','e','r','t','y','u','i','o','p'}
        #set2 = {'a','s','d','f','g','h','j','k','l'}
        #set3 = {'z','x','c','v','b','n','m'}
        table = [1,2,2,1,0,1,1,1,0,1,1,1,2,2,0,0,0,0,1,0,0,2,0,2,0,2]
        
        index = 0
        res = []
        for word in words:
            index = table[ord(word[0].lower()) - ord('a')]
            n = len(word)
            isValid = True
            for i in range(n):
                if table[ord(word[i].lower()) - ord('a')] != index:
                    isValid = False
                    break
            if isValid:
                res.append(word)

        return res


        # 方法二：集合比较
        # 时间复杂度：O(L)，L为所有单词的总长度
        # 空间复杂度：O(1)
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')

        res = []
        for word in words:
            tmp_word = word.lower()
            set_tmp = set(tmp_word)
            #print(set_tmp)
            if set_tmp <= set1 or set_tmp <= set2 or set_tmp <= set3:
                res.append(word)

        return res



                     
