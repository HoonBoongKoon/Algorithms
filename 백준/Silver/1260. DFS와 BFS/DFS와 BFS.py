import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()


visited_d = [False] * (n+1)
visited_b = [False] * (n+1)
result_d = []
result_b = []
def dfs(graph,v):
    visited_d[v]=True
    result_d.append(v)
    for i in graph[v]:
        if not visited_d[i]:
            dfs(graph,i)

def bfs(graph,v):
    queue = deque()
    queue.append(v)
    visited_b[v] = True
    while queue:
        i = queue.popleft()
        result_b.append(i)
        for j in graph[i]:
            if visited_b[j] == False:
                queue.append(j)
                visited_b[j] =True

dfs(graph,v)
bfs(graph,v)

for i in result_d:
    print(i,end=' ')
print()
for i in result_b:
    print(i, end=' ')