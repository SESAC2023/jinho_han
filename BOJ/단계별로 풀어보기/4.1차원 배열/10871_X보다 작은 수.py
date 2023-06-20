import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))


for i in data:
    if i < X:
        print(i, end=' ')
