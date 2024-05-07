
def get_primes(n):
    res = [2, 3]
    for i in range(3, n + 1, 2): 
        switch = True
        for n in res: 
            if n ** 2 > i: 
                break 
            if i % n == 0: 
                switch = False
                break 
        if switch: 
            res.append(i)
    return res


def solver(grid): 
    memo = {}
    x_len = len(grid) 
    y_len = len(grid[0])
    def dfs(val, x, y): 
        if x == 0 and y == 0: 
            return get_gcd(val, grid[x][y])
        if x < 0 or x >= x_len or y < 0 or y >= y_len: 
            return 0
        if (val, x, y) in memo: 
            return memo[(val, x, y)]
        right = 0
        down = 0 
        if y > 0: 
            right = get_gcd(val, grid[x][y - 1])
            right = dfs(right, x, y - 1)
        if x > 0: 
            down = get_gcd(val, grid[x-1][y])
            down = dfs(down, x - 1, y)
        memo[(val, x, y)] = max(right, down)
        return memo[(val, x, y)]
    return dfs(grid[-1][-1], x_len - 1, y_len - 1)
        

gcd = {} 
def get_gcd(a, b): 
    if (a,b) in gcd: 
        return gcd[(a, b)]
    if (b, a) in gcd: 
        return gcd[(b, a)]
    if a == 0: 
        gcd[(a, b)] = b
        return b
    gcd[(a, b)] = get_gcd(b%a, a)
    return gcd[(a, b)]

primes = [] 
def old_get_gcd(a, b): 
    if (a,b) in gcd: 
        return gcd[(a, b)]
    gcd[(a,b)] = 1 
    a_tmp, b_tmp = a, b 
    for prime in primes: 
        if prime > min(a_tmp, b_tmp): 
            break 
        while a_tmp % prime == 0 and b_tmp % prime == 0: 
            gcd[(a, b)] *= prime 
            a_tmp //= prime 
            b_tmp //= prime 
    return gcd[(a, b)]




t = int(input())
for i in range(t): 
    n, m = [int(_) for _ in input().split(" ")]
    grid = [] 
    for j in range(n): 
        grid.append([int(_) for _ in input().split(" ")])
    print(solver(grid))