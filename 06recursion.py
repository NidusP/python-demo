# 1 1 2 3 5 8 13 21 34
def fibonacci(index):
    if(index < 0):
        print('请输入大于0的数!')
        return 0
    if index == 1 or index == 2:
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)

# fibonacci(4)  f(3) + f(2) => f(2) + f(1) + 1 => 2 + 1 = 3
# f(5) f(4) + f(3) => 3 + 2 => 5
print(fibonacci(9))


#  1*2*3*4
def factorial(num):
    if(num < 0):
        print('请输入大于0的数!')
        return 0
    if num == 1:
        return 1
    return num*factorial(num-1)

print(factorial(4))