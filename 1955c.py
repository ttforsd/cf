from collections import deque

def solver(ships, k): 
    ships = deque(ships) 
    res = 0 
    while ships: 
        if len(ships) == 1 and k >= ships[0]: 
            return res + 1 
        elif len(ships) == 1: 
            return res 
        m = min(ships[0], ships[-1])
        if k >= 2 * m: 
            k -= 2 * m
            ships[0] -= m
            if ships[0] == 0: 
                ships.popleft() 
                res += 1
            if not ships: 
                return res
            ships[-1] -= m
            if ships[-1] == 0: 
                ships.pop() 
                res += 1 
        elif k == 2 * m - 1 and ships[0] == m: 
            return res + 1 
        else: 
            return res 
    return res 


print(solver([5,2], 7))


t = int(input())
for _ in range(t): 
    n, k = [int(j) for j in input().split(" ")]
    ships = [int(s) for s in input().split(" ")]
    print(solver(ships, k))