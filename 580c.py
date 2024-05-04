from collections import defaultdict, deque
def solver(cats, graph, m):
    graph = make_graph(graph) 
    res = 0 
    queue = deque([(1, m)])
    visited = set() 
    while queue: 
        cur, remain = queue.popleft() 
        visited.add(cur)
        if cats[cur - 1] == "1": 
            remain -= 1 
        else: 
            remain = m
        if remain < 0: 
            continue
        count = 0 
        for nei in graph[cur]: 
            if nei not in visited: 
                queue.append((nei, remain))
                count += 1 
        if count == 0: 
            res += 1
    return res

def make_graph(edges): 
    graph = defaultdict(set)
    for a, b in edges: 
        graph[a].add(b)
        graph[b].add(a)
    return graph 



n, m = [int(_) for _ in input().split(" ")]
cats = input().split(" ")
edges = [] 
for i in range(n - 1): 
    edges.append([int(_) for _ in input().split(" ")])
print(solver(cats, edges, m))