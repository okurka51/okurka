from math import floor
import random

list = [random.randrange(0,100) for i in range(100)]
list.sort()

num = random.randrange(0,100)

def binaryS(list, num):
    start = 0
    end = len(list)

    while start <= end:
        mid = floor((start+end)/2)

        if list[mid] == num:
            return mid

        if list[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    else:
        if list[start] < num:
            return list[start+1]
        return list[start]


print(list)
print(num)
print(binaryS(list, num))