# -*- coding:utf-8 -*-
# 算术运算符 + - * /  
# % 取余  %=
# ** 幂运算 **=
# // 取整除 //=
print(3//2)
a = 'a'
b = f'{a} b'
c = '{} b c'.format(a)
d = '{ss} b c'.format(ss = a)
print(b)
print(b)
print(b)

# 逻辑运算符 and or not
x = True
y = False
print(x and y, x or y, not y)

# 二进制与位运算  
aa = 125
bb = 0b1111101
print(bin(aa), int(bb))

# 按位与 & 
# 按位或 |
# 按位异或 ^
# 按位取反 ~ 
# 左移 <<  右移 >>


# in  not in  检查是否存在


# id()
dd = aa
print(id(aa), id(dd), aa is dd, dd is not aa)