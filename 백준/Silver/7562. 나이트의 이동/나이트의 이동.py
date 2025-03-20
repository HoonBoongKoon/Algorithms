import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

for _ in range(t):
    size = int(input())
    visited = [[0]*(size) for _ in range(size)]
    start = tuple(map(int,input().split()))
    finish = tuple(map(int,input().split()))

    if start ==finish:
        print(0)
        continue
    queue = deque()
    queue.append([start[0],start[1],0])
    visited[start[0]][start[1]] = 1
    while queue:
        temp = queue.popleft()
        x = temp[0]

        y = temp[1]

        moves = temp[2]

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or ny<0 or nx>=size or ny>=size:
                continue
            if visited[nx][ny]==1:
                continue
            if (nx,ny) == finish:
                print(moves+1)
                queue = deque()
                break
            visited[nx][ny]=1
            queue.append([nx,ny,moves+1])

    