import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph =[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
visited = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            start = (i,j)


queue = deque()
queue.append(start)

da = [-1,1,0,0] #세로
db = [0,0,-1,1] #가로
visited[start[0]][start[1]]=0
while queue:
    a,b = queue.popleft()

    for i in range(4):
        na = a+da[i]
        nb = b+db[i]

        if na<0 or nb<0 or na>=n or nb>=m :
            continue
        if graph[na][nb]==0:
            continue
        if visited[na][nb]!=-1:
            continue
        visited[na][nb] = visited[a][b]+1
        queue.append((na,nb))


for i in range(n):
    for j in range(m):
        if graph[i][j] ==0:
            print(0,end=' ')
        else:
            print(visited[i][j], end=' ')
    print()