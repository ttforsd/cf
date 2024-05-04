def solver(coins):
    res = False 
    for coin in coins: 
        if coin == "U": 
            res = not res 
    return res


n = int(input())
for i in range(n): 
    x = input()
    coin = input()
    if solver(coin) == True: 
        print("YES")
    else: 
        print("NO")
