import sys
from math import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
print(gcd(n,m))
print((n*m) // gcd(n,m))