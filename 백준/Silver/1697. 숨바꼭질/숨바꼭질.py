import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

visited = [0] *100001
queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x==k:
        print(visited[x])
        break
    if x-1 >=0 :
        if visited[x-1] ==0:
            visited[x-1]=visited[x]+1

            queue.append(x-1)
    if x+1< 100001:
        if visited[x+1] ==0:
            visited[x+1] = visited[x]+1

            queue.append(x+1)
    if x*2 <100001:
        if visited[x*2] ==0:
            visited[x*2] = visited[x]+1

            queue.append(x*2)