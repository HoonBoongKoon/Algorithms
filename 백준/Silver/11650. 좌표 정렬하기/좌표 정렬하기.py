#11650 좌표정하기
a=int(input())
b=[]
for i in range(a):
  b.append(list((input().split())))
b.sort(key = lambda x: ( int(x[0]), int(x[1])))
for i in range(a):
  print(b[i][0],b[i][1])