'''
正则表达式demo
'''

import re

print('\n==== start ==== \n')

print(re.findall(r'\d+', '123 12 1 1234 12345'))

searchRes = re.search(r'\d+', 'aaaaaa  123')

if searchRes:
    print("search success")
    print(searchRes)
    print(searchRes.span())
    print(searchRes.start())
    print(searchRes.group(0))
else:
    print("search fail")

print("==== url 测试 (match)  ====")

urlRegex = re.compile("http[s]?://([a-zA-Z0-9\-]+\.)+([a-zA-Z0-9\-]+)")

print(urlRegex.match("http://www.baidu.com"))
print(urlRegex.match("https://www.baidu.com"))
print(urlRegex.match("https://baidu.com"))
print(urlRegex.match("https://baidu."))
print(urlRegex.match("https://baidu"))
print(urlRegex.match("https://baidu.com/"))
print(urlRegex.match("www.baidu.com"))

print("==== url 测试 (search) ====")

print(urlRegex.search("http://www.baidu.com"))
print(urlRegex.search("https://www.baidu.com"))
print(urlRegex.search("https://baidu.com"))
print(urlRegex.search("https://baidu."))
print(urlRegex.search("https://baidu"))
print(urlRegex.search("https://baidu.com/index.html"))
print(urlRegex.search("www.baidu.com"))

print("==== url 测试 (fullmatch) ====")

print(urlRegex.fullmatch("http://www.baidu.com"))
print(urlRegex.fullmatch("https://www.baidu.com"))
print(urlRegex.fullmatch("https://baidu.com"))
print(urlRegex.fullmatch("https://baidu."))
print(urlRegex.fullmatch("https://baidu"))
print(urlRegex.fullmatch("https://baidu.com/index.html"))
print(urlRegex.fullmatch("www.baidu.com"))

print("==== url 测试 (Match Objects) ====")


urlMatch = urlRegex.findall("http://www.baidu.com http://www.sina.com http://www.1688.com http://www.taobao.com")
print(type(urlMatch))
# findall 返回一个tuple(元组)数组
for item in urlMatch[:]:
    print(item)
    print(type(item))
    for s in item[:]:
        print(s)
    print("================")

print('\n==== over ==== \n')
