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