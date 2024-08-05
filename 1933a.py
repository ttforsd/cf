from bisect import bisect_left

def solver(arr): 
    arr.sort() 
    index = bisect_left(arr, 0)
    return - sum(arr[: index]) + sum(arr[index: ])



t = input() 
for _ in range(int(t)): 
    n = input() 
    arr = [int(_) for _ in input().split(" ")]
    print(solver(arr))