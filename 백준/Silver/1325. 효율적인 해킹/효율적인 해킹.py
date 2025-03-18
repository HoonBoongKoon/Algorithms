import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().strip().split())
    graph[b].append(a)



def bfs(graph,start):
    visited=[False ] *(n+1)
    queue=deque()
    queue.append(start)
    visited[start]=True
    cnt=1
    while queue:
        computer = queue.popleft()
        for i in graph[computer]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt+=1
    return cnt

max=0
result=[]
for i in range(1,n+1):
    sum = bfs(graph, i)
    if sum>max:
        result=[i]
        max=sum
    elif sum==max:
        result.append(i)


for i in result:
    print(i,end=' ')