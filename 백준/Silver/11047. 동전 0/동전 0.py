n,k=map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))

coins.reverse()
cnt=0
for i in coins:
    if k>=i:
        cnt+=k//i
        k%=i

print(cnt)