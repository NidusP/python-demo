add = lambda x, y: x+y

func = lambda d:'+' if d > 0 else '-'
print(add(2,6))

print(func(2))
print(func(-6))



# 闭包 closure
def person():
    pay = 0
    def work():
        nonlocal pay
        pay += 10
        return pay
    return work

work = person()
work()
work()
work()
work()
work()
print(work())


# 回调
def func(x, y, f):
    return f(x, y)

print(add(1,3))