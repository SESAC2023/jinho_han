import sys

T = int(input())
for i in range(T):
    data = sys.stdin.readline().rstrip()
    print(data[0]+data[-1])
