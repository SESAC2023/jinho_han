import sys

result = 1
while result > 0:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    result = a+b
    if a+b == 0:
        continue
    else:
        print(a+b)
