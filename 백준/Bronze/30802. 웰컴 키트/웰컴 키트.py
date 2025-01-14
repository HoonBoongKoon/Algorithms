n=int(input())
list=list(map(int,input().split()))
t,p=map(int,input().split())

resulta = 0
for i in list:
    if i == 0:
        continue
    elif (i%t)==0:
        resulta += (i//t)
    else:
        resulta += (i//t)+1

resultb = n//p
resultc = n%p

print(resulta)
print(resultb, resultc)