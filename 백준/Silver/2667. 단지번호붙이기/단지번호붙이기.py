import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

visited = [[-1]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    if visited[x][y]!=-1:
        return -1
    if graph[x][y]==0:
        return -1
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))
    result =1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:

                continue
            if visited[nx][ny]!=-1:

                continue
            if graph[nx][ny]==0:


                continue

            visited[nx][ny] = 1
            queue.append((nx,ny))
            result+=1
    return result

def asdf():
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt+=graph[i][j]
    if cnt ==0:
        print(0)
        return 
    
    l =[]
    for i in range(n):
        for j in range(n):
            temp = bfs(i,j)
            if temp !=-1:
                l.append(temp)

    l.sort()
    print(len(l))
    for i in l:
        print(i)
asdf()