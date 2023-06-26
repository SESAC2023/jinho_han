import sys

N = int(input())
for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
