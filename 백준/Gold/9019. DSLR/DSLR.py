from collections import deque
import sys
input = sys.stdin.readline

dslr=['d','s','l','r']

def d(n):
    if n*2>9999:
        return (n*2)%10000
    return n*2

def s(n):
    if n==0:
        return 9999
    return n-1

def l(n):
    return n//1000 + (n%1000)*10

def r(n):
    return n//10 +(n%10)*1000

def bfs(n, target):
    queue = deque()
    queue.append((n, ''))
    visited = [False for _ in range(10001)]
    visited[n] = True
    while queue:
        x, cmd = queue.popleft()

        if x ==target:
            return cmd
        
        for nx, op in [(d(x),'D'), (s(x),'S'), (l(x),'L'), (r(x),'R')]:
            if not visited[nx]:
                visited[nx] = True
                queue.append((nx,cmd+op))

t = int(input())
for _ in range(t):
    a,b = map(int, input().rstrip().split())
    print(bfs(a,b))