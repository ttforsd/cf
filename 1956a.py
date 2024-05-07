from collections import deque 

def solver(stones): 
    stones = set(stones) 
    stones = list(stones)
    stones.sort()
    d_stones = deque() 
    d_stones.append(stones[0])
    for i in range(1, len(stones)): 
        d_stones.append(stones[i] - stones[i - 1])
    winner = True
    while d_stones: 
        if len(d_stones) == 1: 
            return winner 
        if d_stones[0] > 1: 
            return winner 
        winner = not winner
        d_stones.popleft() 




t = int(input())
for _ in range(t): 
    n = input() 
    stones = [int(s) for s in input().split(" ")]
    if solver(stones): 
        print("Alice")
    else: 
        print("Bob")