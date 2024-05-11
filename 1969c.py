from math import inf 
from heapq import * 
def solver(arr, k): 
    if k == 0: 
        return sum(arr)
    dp = [[0 for _ in arr] for i in range(k + 1)] # stores diff compared to ummod 
    static = [[0 for _ in arr] for i in range(k + 1)] 
    for i in range(1, len(dp)): 
        s = 0 
        pq = []
        for j in range(len(dp[0])): 
            s += arr[j] 
            heappush(pq, (arr[j], j))
            while pq and pq[0][-1] < j - i: 
                heappop(pq) 
            if j - i > 0: 
                s -= arr[j - i - 1]
            if j - i >= 0: 
                dp[i][j] = s - pq[0][0] * (i + 1)
                static[i][j] = s - pq[0][0] * (i + 1)
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0: 
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            for ii in range(1, i): 
                if j - ii - 1 < 0: 
                    break
                tmp = static[ii][j] + dp[i - ii][j - ii - 1] 
                dp[i][j] = max(dp[i][j], tmp)
    return sum(arr) - dp[-1][-1]
# arr = [1,2]
# k = 3
# print(solver(arr, k))



t = int(input()) 
for _ in range(t): 
    k = int(input().split(" ")[-1])
    arr = [int(_) for _ in input().split(" ")]
    print(solver(arr, k))