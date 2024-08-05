from collections import defaultdict

def solver(arr): 
    s = 0 
    counts = defaultdict(int)
    for n in arr:
        tmp = n % 3 
        counts[tmp] += 1
        s += tmp 
    s %= 3
    if s == 0: 
        return 0 
    elif s == 1 and counts[1] != 0: 
        return 1 
    elif s == 1: 
        return 2 
    else: 
        return 1

t = int(input()) 
for _ in range(t): 
    input()
    arr = [int(_) for _ in input().split(" ")]
    print(solver(arr))