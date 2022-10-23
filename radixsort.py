#program to sort the elements using radix sort..
def num_digits(arr):
    maxno = 0
    for num in arr:
        maxno= max(maxno, num)
    return len(str(maxno))
from functools import reduce
def flatten(arr):
    return reduce(lambda x, y: x + y, arr)
 
 
def radix(arr):
    digits = num_digits(arr)
    for digit in range(0, digits):
        temp = [[] for i in range(10)]
        for item in arr:
            num = (item // (10 ** digit)) % 10
            temp[num].append(item)
        arr = flatten(temp)
    return arr
 
 
array = [55, 45, 3, 289, 213, 1, 288, 53, 2]
array = radix(array)
print(array)
