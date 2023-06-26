import sys

num = int(input())
for i in range(num):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
