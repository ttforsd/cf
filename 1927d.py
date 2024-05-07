from bisect import bisect_left, bisect_right

def process_arr(nums): 
    res = [] 
    for i, n in enumerate(nums): 
        if not res or nums[res[-1]] != n: 
            res.append(i)
        else: 
            res[-1] = i 
    return res 


def solver(nums, p_nums, l, r): 
    l_res = bisect_left(p_nums, l)
    r_res = bisect_left(p_nums, r)
    if l_res == r_res: 
        return -1, -1 
    elif nums[p_nums[l_res]] == nums[p_nums[r_res]]: 
        l_res += 1 
    if r < p_nums[r_res]: 
        return p_nums[l_res] + 1, r + 1
    return p_nums[l_res] + 1, p_nums[r_res] + 1


t = int(input())
for _ in range(t): 
    n = input() 
    nums = [int(_) for _ in input().split(" ")]
    p_nums = process_arr(nums) 
    q = int(input())
    for _ in range(q): 
        l, r = input().split(" ")
        l = int(l) - 1
        r = int(r) - 1
        res = solver(nums, p_nums, l, r)
        print(res[0], res[-1])
    print()