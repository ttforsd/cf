def solver(a, b, l): 
    small = min(a, b) 
    large = max(a, b)
    while large != 0 and large % small == 0: 
        large //= small 
    res = 0
    if large == 1: 
        while l % small == 0: 
            l //= small 
            res += 1 
        return res + 1 

    x = 0 
    while l % (a ** x) == 0: 
        y = 0 
        while (l // (a ** x)) % (b ** y) == 0: 
            y += 1 
        res += y 
        x += 1 
    return res 


t = int(input())
for _ in range(t): 
    a, b, l = [int(_) for _ in input().split(" ")]
    print(solver(a, b, l))