import sys

sys.setrecursionlimit(5000)

def process(arr): 
    arr.sort() 
    ar = [] 
    for i, n in enumerate(arr): 
        if i == 0: 
            ar.append(1)
            continue 
        if n == arr[i - 1]: 
            ar[-1] += 1 
        else: 
            ar.append(1)
    return ar 

def rec_solver(arr): 
    arr = process(arr)
    l = len(arr) 
    dp = {}


    def recur(i, moves): 
        if i == l: 
            return 0 
        if (i, moves) in dp: 
            return dp[(i, moves)]
        dp[(i, moves)] = recur(i + 1, moves + 1)
        if arr[i] <= moves: 
            dp[(i, moves)] = max(1 + recur(i + 1, moves - arr[i]), dp[(i, moves)]) 
        return dp[(i, moves)]

    return l - recur(0, 0)

def solver(arr): 
    arr = process(arr) 
    if len(arr) == 1: 
        return 1
    dp = [[0] * (i + 1) for i in range(len(arr))]
    for i in range(1, len(dp)): 
        for j in range(1, len(dp[i])): 
            if j >= arr[i]: 
                dp[i][j] = 1 
            if j > arr[i]: 
                dp[i][j] = max(dp[i][j], 1 + dp[i-1][j- 1 - arr[i]])
            if j < len(dp[i - 1]): 
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0: 
                dp[i][j] = max(dp[i][j], dp[i][j-1])
    return len(arr) - dp[-1][-1]


res = [] 
cases = int(input())
for i in range(cases): 
    n = input() 
    arr = input().split(" ")
    arr = [int(_) for _ in arr]
    print(solver(arr))