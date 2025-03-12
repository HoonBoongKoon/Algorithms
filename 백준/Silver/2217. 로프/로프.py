n=int(input())
k = [int(input()) for _ in range(n)]

k.sort(reverse=True)

max=0
for i in range(len(k)):
    if (i+1)*k[i]>max:
        max=(i+1)*k[i]

print(max)