def add(x = 1, y = 2, *z, name, **aa):
    print(x, x, z, name, aa)
    return aa
print(add(5, 5, 10, 12, aa = 'aa', bb = 'bb', cc = 'cc',name='zhangsan'))


#  global
a = 'global a'
def func():
    global a,b
    a += ' in func '
    b = 'func b'
    c = a+b
    print(c)
    # 获取全局与局部变量
    print('globals():    ', globals())
    print('locals():     ', locals())
func()

print(a, b)


# nonlocal  使用上层的局部变量

def outer():
    num = 1
    a = 10
    def inner():
        nonlocal a
        a += num
        print(num)
    inner()
    print(a)
outer()



def nine(code=0):
    if code > 0:
        xrange = range(1, 10)
    else: 
        xrange = range(9, 0, -1)
    for x in xrange:
        for y in range(1, x + 1):
            print(f'{x}*{y}={x*y}  ' ,end='')
        print()    
print()
nine(1)
print()
print()
nine(-1)
print()

def rectangle(code = 0):
    count = 10
    for x in range(0, count):
        for y in range(0, count):
            if(code <= 0 and x > 0 and x < count - 1 and y != 0 and y != count - 1):
                print(' ', end='')
          
            else: 
                print('#', end='')
        print()
rectangle(-1)
print()
rectangle(1)

