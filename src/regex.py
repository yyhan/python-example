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



# IndexError: no such group
# print(searchRes.group(1))

print('\n==== over ==== \n')
