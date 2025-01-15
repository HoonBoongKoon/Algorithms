#1978소수찾기

a=[]
for i in range(1001):
  a.append(i)
  if i>1:
    for j in range(2,i):
      if i%j==0:
        a[i]=0
        break
a=list(set(a))
a.sort()
a.remove(0)
a.remove(1)

b=int(input())
c=list(map(int,input().split()))
count=0
for i in c:
  if i in a:
    count+=1
print(count)