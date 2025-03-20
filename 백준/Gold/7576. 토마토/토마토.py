import sys
from collections import deque
input = sys.stdin.readline



def asdf():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]   
    m,n = map(int, input().split())

    graph=[]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    # 안 익은 토마토 갯수 세기
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] ==0:
                cnt+=1
    if cnt==0:
        print(0)
        return 0

    v = [[-1] * m for _ in range (n)]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] ==1:
                queue.append((i,j))
                v[i][j] =0
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:

                continue
            if v[nx][ny]!=-1:

                continue
            if graph[nx][ny]==-1:

                continue

            cnt-=1
            v[nx][ny] = v[x][y]+1
            queue.append((nx,ny))

    if cnt==0:
        print(v[x][y])
    else:
        print(-1)

asdf()