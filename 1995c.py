from math import log2 as log, ceil 

def solver(arr):
    res = 0 
    for i in range(1, len(arr)): 
        if arr[i] >= arr[i - 1]:
            continue 
        elif arr[i] == 1: 
            return -1 
        power = ceil(log(log(arr[i-1]) / log(arr[i])))
        res += int(power) 
        arr[i] = arr[i] ** (2 ** power)
    return res 

cases = int(input())

for case in range(cases): 
    n = input() 
    arr = input() 
    arr = arr.split(" ")
    arr = [int(_) for _ in arr]
    tmp = solver(arr) 
    print(tmp) 


# a >= b ^ n 
# log a >= n log b
# n = log b / log a


# a <= b ^ (2 ^ n)
# log a <= (2 ^ n) log b 
# n = log2(log a / log b)