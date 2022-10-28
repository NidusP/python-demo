# -*- coding:utf-8 -*-

a = 10
b = 20
c,d = 5, 10
a,b = b, a
print(a, b, c, d)
# 20 10 5 10
print('变量定义*******************************************')


# string 
s_a = 'this is str'
# 大字符串
s_b = '''this,
is,
str,
'''
s_c = 'c c \nc'
# r使转义字符失效
s_d = r'c c \nc'
print(s_a)
print(s_b)
print(s_c)
print(s_d, type(s_d))
print('string*******************************************')


# number
n_a = 520
n_p = 3.141592653589793
# 16进制
n_b = 0x10
# bytes 是 Python 3.x 新增的类型，在 Python 2.x 中是不存在的
n_c = b'http://c.biancheng.net/python/'
# 复数 complex
n_d = 5 + 6j 
# 布尔类型
n_e = True
n_f = False
print(n_a, type(n_a), 
n_p, type(n_p), 
n_b, type(n_b),
n_c, type(n_c), 
n_d, type(n_d), 
n_e, type(n_e),
n_f, type(n_f),)
print('number*******************************************')


# list 列表/数组
l_a = [1,2,3,['A','B','C'],'a', 'b', 'c']
print(l_a, l_a[0], l_a[-1], type(l_a))
print('list*******************************************')



# tuple 元组 定义元组时, 需要有, 否则就是圆括号表达式
t_a = (1,2,3,('A','B','C'),'a', 'b', 'c')
t_b = 1,2,3,('A','B','C'),'a', 'b', 'c'
print(t_a, t_a[0], t_a[-1], type(t_a))
print(t_b, t_b[0], t_b[-1], type(t_b))

# 元组() 值不可改变  列表[] 值可以改变
l_l=[1,2,3]
l_l[1] = 22
t_t = 1,2,3
# 不可改变 TypeError: 'tuple' object does not support item assignment
# t_t[1] = 22
print(l_l, t_t)
print('tuple*******************************************')



# dict 字典  键值对方式
d_a =  {
    'title': '<<三国演义>>',
    'price': '30.0',
    1: 1,
    2: 2
}
d_a['price'] = 40
print (d_a, type(d_a), d_a['price'])
print('dict 字典*******************************************')



# set 集合  无序且不重复  
s_a= {1,2,3,4,5,6,7,'a', 'b'}
s_a.add(110)
# 空集合
s_b= set()
# 空字典
s_c= {}
print (s_a, type(s_a))
print (s_b, type(s_b))
print (s_c, type(s_c))
s_a.discard(1)
print (s_a, 1 in s_a)
# 集合运算 交集 差集 并集 对称差集
s_e= {1,2,3,4,5}
s_f= {3,4,5,6,7}
print (s_e & s_f)
print (s_e - s_f)
print (s_e | s_f)
print (s_e ^ s_f)
print('set 集合*******************************************')