from bisect import bisect_right, bisect_left

"""
4
5
1 5 4 2 3
3
1 2 3
4
2 1 4 3
6
5 2 4 1 6 3

2
0
1
3

"""

""" 
[1, 2, 4, 3, 5, 6]
[5, 1, 2, 3, 4, 6]

first and last need to be added last 

"""


def solver(arr): 
    mid_pt = (len(arr) + 1) / 2
    small = [] 
    large = [] 
    res = 0 
    for i in range(len(arr) // 2): 
        l = arr[i] 
        r = arr[len(arr) - 1 - l]
        if l > mid_pt: 
            pass 
        elif not small or l > small[-1]: 
            small.append(l) 
        elif small: 
            index = bisect_right(small, l) 
            res = max(res, index) 
            small.insert(index, l) 
        if r < mid_pt: 
            pass
        elif not large: 
            large.append()



         




t = int(input()) 
for i in range(t): 
    l = input() 
    arr = input().split(" ") 
    arr = [int(_) for _ in arr] 
    print(solver(arr)) 

