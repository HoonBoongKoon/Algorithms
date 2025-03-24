import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

n,m = map(int,input().split())
graph =[]
for _ in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

c = []
virus =[]
cnt=-3
for i in range(n):
    for j in range(m):
        if graph[i][j] ==0:
            c.append((i,j))
            cnt+=1
        elif graph[i][j]==2:
            virus.append((i,j))
c = combinations(c,3)



dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(g, walls, q, cnt, present_max):
    visited = [[0] *m for _ in range (n)]
    graph = copy.deepcopy(g)

    for i in walls:
        graph[i[0]][i[1]] = 1

    queue = q

    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if visited[nx][ny] ==1:
                continue
            if graph[nx][ny] !=0:
                continue
            graph[nx][ny] = 2
            cnt-=1
            queue.append((nx,ny))
            if present_max>cnt:
                return 0

    return cnt

result = 0

for i in c:
    queue = deque()
    for j in virus:
        queue.append(j)
    count = cnt
    temp = bfs(graph, i, queue, count, result)
    if result<temp:
        # print(i, '일때 최고로 잘나옴')
        # for x in range(n):
        #     print(graph[x])
        result = temp
print(result)
