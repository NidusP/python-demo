print('****************list')
l_a,l_b = [1,2,3], ['a','b','c']

# 列表拼接  list+list  list*int
print(l_a+l_b, l_a*3, )

# 元素判断  不能通过下标添加元素
l_a[2] = 5
print(1 in l_a, l_a, l_a[0])

# append 末尾追加元素
# del 通过下标删除指定元素  | 或者 pop方法末尾出栈(默认最后一个)
del l_a[0]
print(l_a)

# len 列表长度
print(len(l_a))

# 切片 [start:end:step]  可进行重新赋值   同样可以  del [] 删除切片
# 当步进值不为1时, 赋值的个数要对应替换元素的个数
l_b[::] = 'abcd'
print(l_b, l_b[1:], l_b[:2], l_b[::-1])





# demo
var_dict = { 'user': 'admin', 'age': 18, 'phone': 123 }
var_list = [f'{key}={str(var_dict[key])}' for key in var_dict]
# ['user=admin', 'age=18', 'phone=123']
var_str = '&'.join(var_list)
# user=admin&age=18&phone=123
print(var_str)


var_list = ['AAA', 'BBB', 'CCC']
var_l = [ i.lower() for i in var_list]
# ['aaa', 'bbb', 'ccc']
print(var_l)

# 0-5  x 偶数  y 奇数 组成元组
var_list = [(x, y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 == 1 ]
print(var_list)


# 9*9
var_l = [f'{i}*{j}={i*j}' for i in range(1, 10) for j in range(1, i + 1)]
print(var_l)

'''
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

n = [
    [2,2,2],
    [3,3,3],
    [4,4,4]
]

乘积结果
1 [2,4,6,12,15,18,28,32,36]
2 [[2,4,6],[12,15,18],[28,32,36]]
'''
