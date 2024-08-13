from math import log2 as log, ceil, inf

def solver(arr):
    res = 0 
    addition = [0] * len(arr) 
    arr[0] = log(arr[0])
    if arr[0] != 0: 
        arr[0] = log(arr[0])
    else: 
        arr[0] = -inf 
    for i in range(1, len(arr)): 
        arr[i] = log(arr[i])
        if arr[i] != 0: 
            arr[i] = log(arr[i])
        else: 
            arr[i] = -inf
        if arr[i] >= arr[i - 1] + addition[i - 1]:
            continue 
        elif arr[i] == -inf: 
            return -1 
        power = ceil(arr[i - 1] - arr[i]) + addition[i - 1]
        addition[i] = power
        res += int(power) 
    return res 


cases = int(input())

for case in range(cases): 
    n = input() 
    arr = input() 
    arr = arr.split(" ")
    arr = [int(_) for _ in arr]
    tmp = solver(arr) 
    print(tmp) 

# a <= b ^ (2 ^ n)
# log a <= (2 ^ n) log b 
# n = log2(log a / log b)
# n = log(log(a)) - log(log(b))