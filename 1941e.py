import heapq 


def helper(bridges, k): 
    if k == len(bridges): 
        return sum(bridges)
    tmp = sum(bridges[:k])
    res = tmp 
    for i in range(1, len(bridges) - k + 1):
        tmp = tmp - bridges[i - 1] + bridges[i + k - 1]
        res = min(res, tmp)
    return res  

def dp_solver(row, d): 
    row[0] += 1 
    h = [] 
    heapq.heappush(h, [row[0], 0])
    for i in range(1, len(row)): 
        while h[0][-1] < i - d - 1:
            heapq.heappop(h)
        row[i] += 1 + h[0][0] 
        heapq.heappush(h, [row[i], i])
    return row[-1]
            

def solver(grid, d, k): 
    bridges = []
    for row in grid: 
        bridges.append(dp_solver(row, d))
    return helper(bridges, k)
        


t = int(input())
for _ in range(t): 
    n, m, k, d = [int(_) for _ in input().split(" ")]
    grid = [] 
    for i in range(n): 
        grid.append([int(_ ) for _ in input().split(" ")])
    print(solver(grid, d, k))