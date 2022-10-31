# range start, end, step
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