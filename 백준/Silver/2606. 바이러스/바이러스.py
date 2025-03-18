import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(m):
    collections = (list(map(int, sys.stdin.readline().split())))
    graph[collections[0]].append(collections[1])
    graph[collections[1]].append(collections[0])

def dfs(graph, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)


visited = [False] * (n+1)

dfs(graph,1)

result = sum(visited) -1

print(result)