from itertools import count


a = 0
b = 1
if a or b:
    print('true')
else:
    print('false')

year = input('请输入年份: ')
if int(year) % 400:
    print(year, '年是平年')
else:
     print(year, '年是闰年')


# 🌟 ✨

# 隔行换色
index = 1
while index <= 100:
    if ((index + 9)//10) % 2:
        print('🌟', end='')
    else:
        print('✨', end='')
    if (index%10 == 0):
        print()
    index += 1 
print()
print('**************************')
print()
num = 1
while num <= 100:
    if (num%2):
        print('🌟', end='')
    else:
        print('✨', end='')
    if (num%10 == 0):
        print()
    num += 1 

# 9*9
for x in range(9, 0, -1):
    for y in range(x, 0, -1):
        print(f'{x}*{y}={x*y}  ' ,end='')
        if(y == 1):
            print()

print()
print('*****************************')
print()
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f'{y}*{x}={x*y}  ' ,end='')
        if(y == x):
            print()

print()
print('*****************************')
print('斐波那契数列')
# 0 1 1 2 3 5 8 13
nums = int(input('请输入数列位置索引?'))

n1 = 0
n2 = 1
index = 2
if nums < 1:
    print('请输入大于0的整数!')
elif nums == 1:
    print(n1)
elif nums == 2:
    print(n2)
else:
    print(n1, n2, end=' ')
    while index < nums:
        n3 = n1+n2
        print(n3, end=' ')
        n1,n2 = n2,n3
        index += 1


print()
print('*****************************')
print('''
公鸡-3  母鸡-1 小鸡-0.5, 100元买100只鸡, 有几种方案?
''')
count = 0
for gj in range (1, 34):
    for mj in range (1, 101):
        xj = 100 - gj - mj
        if(gj*3 + mj*1 + xj*0.5 == 100):
            count += 1
            print(f'公鸡{gj}只, 母鸡{mj}只, 小鸡{xj}只')
print(f'{count}种方案! ')