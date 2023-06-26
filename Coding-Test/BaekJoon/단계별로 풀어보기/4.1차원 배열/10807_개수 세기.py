import sys

N = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(input())

print(data.count(v))
