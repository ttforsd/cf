def solver(n, m, a, b): 
    if b / m >= a: 
        return a * n 
    return n // m * b + min(n % m * a, b)



n, m, a, b = input().split(" ")
n, m, a, b = int(n), int(m), int(a), int(b)
print(solver(n, m, a, b))