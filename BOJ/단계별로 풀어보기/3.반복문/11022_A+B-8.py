import sys

N = int(input())
for i in range(1, N+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i,a,b,a+b))
