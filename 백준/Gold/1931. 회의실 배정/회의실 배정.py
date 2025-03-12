import sys
n=int(sys.stdin.readline().strip())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort(key = lambda x:(x[1],x[0])) # 끝 순서대로 정렬

cnt=1
last_end_time = arr[0][1]
for i in range(1,n):
    if arr[i][0]>=last_end_time:
        cnt+=1
        last_end_time = arr[i][1]
print(cnt)