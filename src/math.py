'''
math example

'''

print(1 + 2)
print(2 * 3)
print(4 / 2)

print(0 / 4)
print(2 / 3)

# ZeroDivisionErroxdr: division by zero
# print(4 / 0)

print(abs(-2))

# 指数运算
print(pow(2, 3))
print(pow(4, -1))
print(pow(4, -2))
print(pow(0, 2))
# ZeroDivisionError: 0.0 cannot be raised to a negative power
# print(pow(0, -2))

# float 方法将字符转换为float类型
print(float('0.003'))
print(float('+0.003'))
print(float('-0.003'))
print(float('-0.003    '))
print(float('-0.003    \n'))
print(float('-0.003    \n\t'))
print(float('Infinity')) # Infinity 无穷

# round 方法提供四舍五入算法
print('round(4.1000000001)=%s'%(round(4.1000000001)))
print('round(4.4000000001)=%s'%(round(4.4000000001)))
print('round(4.5000000000)=%s'%(round(4.5000000000)))
print('round(4.5000000001)=%s'%(round(4.5000000001)))
print('round(4.5000000001, 1)=%s'%(round(4.5000000001, 1)))
print('round(4.5000000001, 2)=%s'%(round(4.5000000001, 2)))
print('round(4.5050000000, 2)=%s'%(round(4.5050000000, 2)))
print('round(4.5050000001, 2)=%s'%(round(4.5050000001, 2)))


print(any([False, True, False, False]))
print(all([False, True, False, False]))
