import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
test_case = int(input())

def dfs(graph, x,y,n,m):
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(graph,x-1,y,n,m)
        dfs(graph,x,y-1,n,m)
        dfs(graph,x+1,y,n,m)
        dfs(graph,x,y+1,n,m)
        return True
    return False
    
    
def test():
    n,m,k = map(int, input().split())
    graph = [[0] * (m) for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x][y] =1
        
             
    result =0
    for i in range(n):
        for j in range(m):
            if dfs(graph,i,j,n,m)==True:
                result+=1
    print(result)

for i in range(test_case):
    test()