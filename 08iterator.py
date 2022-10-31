from typing import Iterable, Iterator


arr = [1,2,3,4,5,6,7,8,9,10]

for i in arr:
    print(i, end=' ')


arrI = iter(arr)

print(arrI, type(arrI), isinstance(arr, Iterable), isinstance(arr, Iterator), )

while len(arr) > 0:
    arrI = iter(arr)
    data = next(arrI)
    arr = list(arrI)
    print(data)


