a=int(input())
b=[]
for i in range(a):
    b.append(input()) 
setb=set(b)
b=list(setb)

b.sort()
b.sort(key=len)

for i in b:
    print(i)