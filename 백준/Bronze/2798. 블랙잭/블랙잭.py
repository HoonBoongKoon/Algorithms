n,m=map(int,input().split())
a= list(map(int, input().split()))
a.sort()

result=0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if i!=j and j!=k and i!=k:
                l=a[i]+a[j]+a[k]
                if l>result and l<=m:
                    result = l

print(result)