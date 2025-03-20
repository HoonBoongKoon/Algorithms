import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)


for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x,visited):
    if visited[x]!=0:
        return False
    visited[x] =1
    queue = deque()
    queue.append(x)
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i]!=0:
                continue
            visited[i] = 1
            queue.append(i)
    return True


cnt=0
for i in range(1,n+1):
    if bfs(i,visited) ==True:
        cnt+=1

print(cnt)