from collections import deque

def solver(n, m): 
    queue = deque([(n, 0)])
    visited = set() 
    while queue: 
        cur, steps = queue.popleft() 
        if cur == m: 
            return steps 
        if cur in visited or cur <= 0: 
            continue 
        visited.add(cur)
        if cur < m:
            queue.append((cur * 2, steps + 1))
        queue.append((cur - 1, steps + 1))


n, m = input().split(" ") 
n, m = int(n), int(m) 
print(solver(n, m))