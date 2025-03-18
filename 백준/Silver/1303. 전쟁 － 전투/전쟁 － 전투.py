import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(n):
    string = list(input().strip())
    for c in range(m):
        graph[i].append(string[c])

visited = [[False] * m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(a,b):
    if visited[a][b] ==True:
        return 0,0
    cnt=1
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True
    team = graph[a][b]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == team:
                queue.append((nx,ny))
                visited[nx][ny] = True
                cnt+=1

    return team,cnt*cnt

w = 0
b = 0

for i in range(n):
    for j in range(m):
        team,cnt = bfs(i,j)
        if team == 'W':
            w+=cnt
        elif team =='B':
            b+=cnt

print(w, b)