# range start, end, step
from functools import reduce
from typing import Iterable, Iterator

ten = range(10)
_ten = range(10, 0, -1)
print(ten, type(ten), list(_ten), isinstance(ten, Iterable), isinstance(ten, Iterator))


# zip 聚合多个可迭代对象, 按索引组合为元组  *zip 组合好的数据
a ,b,c= [1, 2, 3], ['a', 'b', 'c'], 'DEF'
l_zip = zip(a ,b,c)

list_a = [*zip(a ,b,c)]
print(list_a[0], list_a[0] == list(l_zip)[0]) 
# (1, 'a', 'D') True
# [(1, 'a', 'D'), (2, 'b', 'E'), (3, 'c', 'F')]


# 类型转换相关
# int
# float
# bool
# complex
# str
# list
# tuple
# dict
# set

# 变量相关
# id   获取变量的id标识
# type 
# print
# input
# isinstance

print('*******number相关***************')
# number相关
print(abs(-1.1))
print(sum([-1.1, 2.2]))
print(min([-1.1, 2.2]), min(-1.1, 2.2))
print(pow(2, 3))
# round  数进偶退
print(round(3.1331231, 2), round(3.5), round(4.5))

# 进制
# 10进制 -> 2进制
print(bin(10), int(0b1010))

# 8进制
print(oct(16), int(0o20))

# 16进制
print(hex(48), int(0x30))


# ASCII码
# 字符 -> ASCII码  ASCII码 -> 字符
print(ord('a'), chr(65))


arr = [1, 54, -1, -9, 0]

# sorted
print('*************sorted')
print(sorted(arr))
print(sorted(arr, reverse=True))
print(sorted(arr, key=abs))
print(sorted(arr, key=lambda x: x %2))

# map
print('*************map')
print(list(map(lambda x: x**2, arr)))

# reduce
print(reduce(lambda x, y: x+y, arr))

# filter
print(list(filter(lambda x: x > 0, arr)))



print('*******str相关***************')
# \n 换行  \t 制表符  \r 光标位置  \b 回退
str = '我以我血荐轩辕\\n凭阑处' + '潇潇雨歇'*3
# [start:end:step]切片 
# 全部步进值为2
print(str)
print(str[::2])
print(str[::-1], str[::-2])

str_a = '杜甫'
str_fa = '{}是诗人, {}'.format(str_a, 'lalala')
print(str_fa)

# 索引传参
str_fa = '{0}是诗人, {1}'.format('lalala', str_a)
print(str_fa)
# 关键字传参
str_fa = '{a}是诗人, {b}'.format(b='lalala', a = str_a)
print(str_fa)
# 容器传参
dict_a = { "a": "aaa", "b": "bbb"}
str_fa = '{a}是诗人, {b}'.format(**dict_a)
print(str_fa)

list_a = ['111', '222']
str_fa = '{a[0]}是诗人, {a[1]}'.format(a=list_a)
print(str_fa)

str_fa = f'{list_a[0]}是诗人, {list_a[1]}'
print(str_fa)

# 限定位数
str_fa = '{:.3f}是诗人'.format(1.23456789)
print(str_fa)

print('*******************************str')
# str
str_v = 'i love you'
str_c = 'I LOVE YOU'
str_a = '  '
# capitalize 生成首字符大写,其余小写的副本 
#   (i love you | I LOVE YOU) -> I love you

# title 将每个单词的首字符大写, 其余小写  istitle 判断是否符合
#   (i love you | I LOVE YOU) -> I Love You

# upper 转为大写  isupper 是否全是大写
#  i love you -> I LOVE YOU

# lower 转为小写 islower 是否全部小写
#  I LOVE YOU -> i love you

# swapcase 反转大小写  
# i love you -> I LOVE YOU -> i love you

# isalnum 是否均为字符(数字/中文/英文)的字符串

# isalpha 是否均为中英文字符(中文/英文)的字符串

# isdigit 是否均为数字字符(数字)的字符串

# isspace 是否均为空白字符(空格)的字符串.

# startswith 指定位置开始(默认index为0)是否为指定字符
# endswith  str, start, end

# len 返回字符串长度

# str in var var中是否包含str

# find(str[, start[, end]]) 返回第一个符合条件的index, 不存在返回 -1
# rfind  从右向左找第一个符合的

# index/rindex  同上, 不过找不到会报错

# count 计算出现次数


# split  分割字符串为列表(可指定分割次数)  i love you -> ['i', 'love', 'you']
# join 字符串作为连接符连接容器中所有元素 list  tuple &...

# rsplit 从右向左分割字符串为列表(可指定分割次数)

# strip 去除字符串左右两侧的指定字符
# lstrip 左侧    rstrip  右侧

# replace 字符替换, 可指定替换次数

# center 按照长度根据指定字符补齐字符串  i ->  **i**

# ljust 放在右侧补齐  rjust 放在左侧补齐


