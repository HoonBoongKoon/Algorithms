import sys

n=int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().strip().split()))
    
max=0
for i in d:
    if max<i:
        max=i

new_d = []
for i in d:
    new_d.append((i/max)*100)
print(sum(new_d)/n)