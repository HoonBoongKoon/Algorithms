import sys
input = sys.stdin.readline

S = set()

n = int(input())


for i in range(n):
    a= input().strip().split()
    if a[0] =='add':
        S.add(int(a[1]))
    elif a[0]=='remove':
        S.discard(int(a[1]))
    elif a[0]=='check':
        b = int(a[1])
        if b in S:
            print(1)
        else:
            print(0)
    elif a[0]=='toggle':
        b = int(a[1])
        if b in S:
            S.remove(b)
        else:
            S.add(b)
    elif a[0]=='all':
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif a[0]=='empty':
        S = set()


