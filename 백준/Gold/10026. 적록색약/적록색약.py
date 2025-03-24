from collections import deque

def bfs(tp):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue.append(tp)
    visited[tp[0]][tp[1]] = 1
    while queue:
        x,y = queue.popleft()
        # visited[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visited[nx][ny]==1:
                continue
            if graph[nx][ny] != graph[tp[0]][tp[1]]:
                continue
            visited[nx][ny] = 1
            queue.append((nx,ny))


n = int(input())
graph = [list(input().strip()) for _ in range(n)]
queue = deque()


visited = [[0] * n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt+=1
            bfs((i,j))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'


visited = [[0] * n for _ in range(n)]
cnt_saekyak = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt_saekyak+=1
            bfs((i,j))
print(cnt, cnt_saekyak)