"""
TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk 。请你设计一个类来加密与解密 TinyURL 。
加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL 可以用解密方法恢复成原本的 URL 。

实现 Solution 类：
Solution() 初始化 TinyURL 系统对象。
String encode(String longUrl) 返回 longUrl 对应的 TinyURL 。
String decode(String shortUrl) 返回 shortUrl 原本的 URL 。题目数据保证给定的 shortUrl 是由同一个系统对象加密的。

示例：
输入：url = "https://leetcode.com/problems/design-tinyurl"
输出："https://leetcode.com/problems/design-tinyurl"

解释：
Solution obj = new Solution();
string tiny = obj.encode(url); // 返回加密后得到的 TinyURL 。
string ans = obj.decode(tiny); // 返回解密后得到的原本的 URL 。
 
提示：
1 <= url.length <= 10^4
题目数据保证 url 是一个有效的 URL

"""

# 方法一：模拟
class Codec:

    def encode(self, longUrl: str) -> str:
        res = ""
        for ch in longUrl:
            res += chr(ord(ch) + 1)
        return res

    def decode(self, shortUrl: str) -> str:
        res = ""
        for ch in shortUrl:
            res += chr(ord(ch) - 1)
        return res


# 方法二：哈希表
class Codec:
    def __init__(self):
        self.dictionary = {}
        self.id = randint(1, 100)

    def encode(self, longUrl: str) -> str:
        #self.id += 1
        self.dictionary[self.id] = longUrl
        #print(self.dictionary)
        #print('http://tinyurl.com/' + str(self.id))
        return 'http://tinyurl.com/' + str(self.id)

    def decode(self, shortUrl: str) -> str:
        index = shortUrl.rfind('/')
        #print(shortUrl[index + 1:])
        return self.dictionary[int(shortUrl[index + 1:])]


# 方法三：哈希生成
K1, K2 = 1117, 10 ** 9 + 7

class Codec:
    def __init__(self):
        self.dataBase = {}
        self.urlToKey = {}

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlToKey:
            return "http://tinyurl.com/" + str(self.urlToKey[longUrl])
        key, base = 0, 1
        for c in longUrl:
            key = (key + ord(c) * base) % K2
            base = (base * K1) % K2
            print('key, base:', key, base)
        while key in self.dataBase:
            key = (key + 1) % K2
        self.dataBase[key] = longUrl
        self.urlToKey[longUrl] = key
        #print('self.dataBase:', self.dataBase)
        #print('self.urlToKey:', self.urlToKey)
        return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind('/')
        key = int(shortUrl[i + 1:])
        return self.dataBase[key]


# 方法四：随机生成
class Codec:
    def __init__(self):
        self.dataBase = {}

    def encode(self, longUrl: str) -> str:
        while True:
            key = randrange(maxsize)
            if key not in self.dataBase:
                self.dataBase[key] = longUrl
                return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind('/')
        key = int(shortUrl[i + 1:])
        return self.dataBase[key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


